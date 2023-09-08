"""
Scikit Example
==============

An example to demonstrate the usage of Howso in "traditional" ML ways.

The howso python package extends the scikit-learn Estimator via the following classes:

* `howso.scikit.HowsoEstimator`
* `howso.scikit.HowsoClassifier`
* `howso.scikit.HowsoRegressor`

HowsoEstimator provides users with a Python interface that follows the
conventions of sklearn estimators. For use of Howso's functionality use
`howso.engine.Trainee`.

This is a simple example on how to use the `howso.scikit.HowsoRegressor`
which extends the `howso.scikit.HowsoEstimator` to fit data and make
predictions based on that data.
"""

import pandas as pd

from pprint import pprint
from howso.scikit import HowsoClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


def main():
    # Read in the data.
    print("Reading breast cancer data set.")
    df = pd.read_csv("data/breast_cancer.csv")

    # Split the dataset into the feature (X) and targets (y)
    X = df.drop('y', axis=1).values.astype(float)
    y = df['y'].values.astype(float)

    le = LabelEncoder()
    le.fit(df['y'])
    y = le.transform(df['y'])

    print(f"Target values encoded from {list(le.classes_)} to "
          f"{list(le.transform(le.classes_))}.")

    # Split the dataset into an 80/20 train/test set.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=True)

    # Create a classifier.
    dp = HowsoClassifier()

    # Fit the training data.
    print("Training on a random selection of 80% of the data.")
    dp.fit(X_train, y_train)

    # Test against the reserved test data.
    print("Scoring against 20% reserve test data:")
    score = dp.score(X_test, y_test)

    # Print the resulting accuracy.
    print(score)

    # Detailed prediction results
    print("Getting details for most similar cases from the first prediction:")
    results = dp.describe_prediction(X_test)
    pprint(results['explanation']['most_similar_cases'][0])

    print("Getting class probabilities and classes for the model:")
    probas = dp.predict_proba(X_test)
    pprint(probas)
    pprint(dp.classes_)

    return score


if __name__ == "__main__":
    main()
