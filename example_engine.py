"""
Howso Engine Example
=========================

An example to showcase the rich explanations from the Howso client.

Howso Engine allows Python users to access Howso's full functionality
with a user friendly API.

Below is an example use of the `howso.engine.Trainee` class. The
example covers the basic steps in a typical Howso workflow:

1. Creation of a trainee.
2. Training.
3. Analyze the trainee.
4. Reaction by the trainee to new data, which produces predicted values for the action features.
5. Extraction of audit data that explains the prediction.
"""

from howso import engine
from howso.utilities import infer_feature_attributes
import pandas as pd
from pprint import pprint


def main():
    # Read in the breast cancer data.
    print("Reading breast cancer data set.")
    df = pd.read_csv("data/breast_cancer.csv")
    # Define features for the trainee.
    features = infer_feature_attributes(df)
    feature_names = df.columns.tolist()
    action_features = feature_names[-1:]
    context_features = feature_names[:-1]

    # Shuffle the data.
    df = df.sample(frac=1).reset_index(drop=True)

    # Split the data into an 80% training set and 20% test set.
    test_percent = 0.2
    data_train = df[:int(len(df) * (1 - test_percent))]
    data_test = df[int(len(df) * -1 * test_percent):]
    # Remove the target column from the test set
    data_test_no_target = data_test.drop(action_features, axis=1)

    # Create the trainee, using a context manager so resources are released
    # once complete.
    with engine.Trainee(features=features) as t:
        # Train the cases into the trainee.
        print("Training on a random selection of 80% of the data.")
        t.train(data_train)
        print(f"Number of trained cases: {t.get_num_training_cases()}")

        # Run analyzation on the trainee.
        print("Analyzing the trainee.")
        t.analyze(context_features, action_features)

        # React to the trainee with the context feature values.
        print("Reacting to 20% reserve test data.")
        details = {'feature_robust_accuracy_contributions': True,
                   'feature_robust_residuals': True,
                   'influential_cases': True,
                   'num_most_similar_cases': 3,
                   'num_boundary_cases': 3,
                   'feature_robust_residuals_for_case': True}
        result = t.react(
            data_test_no_target,
            action_features=action_features,
            context_features=context_features,
            details=details)

        # Retrieve the prediction stats from the trainee
        stats = t.get_prediction_stats(
            prediction_stats_action_feature=action_features[0],
            details={
                "prediction_stats": True,
                "selected_prediction_stats": ['accuracy', 'mae']
            }
        )
        accuracy = stats[action_features[0]]['accuracy']
        mae = stats[action_features[0]]['mae']

    # Print the accuracy of the reaction
    print("Prediction stats:")
    print(f"Accuracy: {accuracy:.1%}")
    print(f"Mean Absolute Error: {mae}")

    # Print a detailed result from audit details.
    print("Printing details for most similar cases from the first prediction:")
    pprint(result['details']['most_similar_cases'][0])

    return accuracy


if __name__ == "__main__":
    main()
