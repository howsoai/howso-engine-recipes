import pandas as pd
from pathlib import Path
from pmlb import fetch_data

import seaborn as sns
import matplotlib.pyplot as plt


from howso.engine import Trainee, load_trainee
from howso.utilities import infer_feature_attributes

import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
import lightgbm as lgbm
from sklearn.metrics import accuracy_score, mean_squared_error

def get_matrices(df, features):
    # Create the Trainee
    t = Trainee(
        features=features,
        overwrite_existing=True
    )

    # Train
    t.train(df)

    # Analyze the Trainee
    t.analyze()

    # Recommended metrics
    mda_df = pd.DataFrame()
    fc_df = pd.DataFrame()
    stats = ['contribution', 'mda']
    # for feature in features:
    for feature in features:
        t.react_into_trainee(action_feature=feature, mda_robust=True, contributions_robust=True)
        robust_mda = t.react_aggregate(action_feature=feature, robust=True, stats=['mda'])
        robust_feature_contributions = t.react_aggregate(action_feature=feature, robust=True, stats=['contribution'])
        robust_mda.index.values[0] = feature
        robust_feature_contributions.index.values[0] = feature
        mda_df = pd.concat([mda_df, robust_mda])
        fc_df = pd.concat([fc_df, robust_feature_contributions])

    def sort_and_norm(df, abs=False):
        df = df.sort_index(axis=0)
        df = df.sort_index(axis=1)
        # row_sums = df.sum(axis=1)
        # df = df.div(row_sums, axis=0)
        df = df.div(df.abs().max(axis=1), axis=0)
        df.fillna(1, inplace=True)
        if abs:
            df = df.abs()
        return df

    mda_df2 = sort_and_norm(mda_df)
    fc_df2 = sort_and_norm(fc_df)

    # mda_df2_abs = sort_and_norm(mda_df, abs=True)
    # fc_df2_abs = sort_and_norm(fc_df2, abs=True)

    corr_matrix = df.corr()
    corr_matrix = corr_matrix.sort_index(axis=0)
    corr_matrix = corr_matrix.sort_index(axis=1)

    return {"mda": mda_df2, "fc": fc_df2, "corr": corr_matrix}

def run_models(X_train, y_train, x_test, model, model_type, features, action_feature):

    def lgbm_model(X_train, y_train, x_test, model, model_type, features, action_feature):
        if model_type == 'continuous':
            model= lgbm.LGBMRegressor(verbose=-1)
        else:
            model = lgbm.LGBMClassifier(verbose=-1)

        model.fit(X_train, y_train)
        predictions = model.predict(x_test)

        return predictions

    def howso_model(X_train, y_train, x_test, model, model_type, features, action_feature):
        train_df = pd.concat([X_train, y_train], axis=1)

        t = Trainee(
            features=features,
            overwrite_existing=True
        )

        action_features = [action_feature]
        context_features = features.get_names(without=action_features)

        t.train(train_df)
        t.analyze()

        results = t.react(x_test[context_features],
                            context_features=context_features,
                            action_features=[action_feature])

        predictions = results['action'][action_feature]

        return predictions

    if model == 'lgbm':
        predictions = lgbm_model(X_train, y_train, x_test, model, model_type, features, action_feature)
    elif model == 'howso':
        predictions = howso_model(X_train, y_train, x_test, model, model_type, features, action_feature)

    return predictions

def feature_keeper(df, column, cutoff='median'):
    data = df[column]
    cutoff_value = data.abs().median()
    # cutoff_value = data.abs().quantile(0.75)
    # Filter indexes based on condition
    filtered_indexes = data[data.abs() > cutoff_value].index
    return list(filtered_indexes)

def run_test(df, features, corr_matrix, model):
    results = {}
    # for action_feature in features:
    for action_feature in ['target']:
        model_type = features[action_feature]['type']

        # Only keep features with strong correlation
        filtered_features = feature_keeper(corr_matrix, action_feature)

        X = df[filtered_features]
        filtered_feature_attributes = infer_feature_attributes(X)

        X = X.drop(columns=action_feature)
        y = df[action_feature]  # Target variable

        # Step 4: Split Data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        prediction = run_models(
            X_train=X_train,
            y_train=y_train,
            x_test=X_test,
            model=model,
            model_type=model_type,
            features=filtered_feature_attributes,
            action_feature=action_feature
        )

        if model_type == 'continuous':
            accuracy = mean_squared_error(y_test, prediction)
            print("MSE:", accuracy)
        else:
            accuracy = accuracy_score(y_test, prediction)
            print("Accuracy:", accuracy)

        results[action_feature] = accuracy

    return results

datasets = ['adult']
dataset_results = {}
for dataset in datasets:
    df = fetch_data(dataset, local_cache_dir=f"data/{dataset}")
    # Subsample the data to ensure the example runs quickly
    df = df.sample(200)
    # Infer features attributes
    features = infer_feature_attributes(df)
    matrices = get_matrices(df, features)
    for metric, matrix in matrices.items():
        if metric != 'fc':
            continue
        full_results = []
        for run in range(5):
            result = run_test(df, features, matrix, 'lgbm')
            full_results.append(result)
        dataset_results[dataset] = full_results


def run_models(X_train, y_train, x_test, model, model_type, features, action_feature):

    def lgbm_model(X_train, y_train, x_test, model, model_type, features, action_feature):
        if model_type == 'continuous':
            model= lgbm.LGBMRegressor(verbose=-1)
        else:
            model = lgbm.LGBMClassifier(verbose=-1)

        model.fit(X_train, y_train)
        predictions = model.predict(x_test)

        return predictions

    def howso_model(X_train, y_train, x_test, model, model_type, features, action_feature):
        train_df = pd.concat([X_train, y_train], axis=1)

        t = Trainee(
            features=features,
            overwrite_existing=True
        )

        action_features = [action_feature]
        context_features = features.get_names(without=action_features)

        t.train(train_df)
        t.analyze()

        results = t.react(x_test[context_features],
                            context_features=context_features,
                            action_features=[action_feature])

        predictions = results['action'][action_feature]

        return predictions

    if model == 'lgbm':
        predictions = lgbm_model(X_train, y_train, x_test, model, model_type, features, action_feature)
    elif model == 'howso':
        predictions = howso_model(X_train, y_train, x_test, model, model_type, features, action_feature)

    return predictions

def feature_keeper(df, column, cutoff='median'):
    data = df[column]
    if cutoff == 'median':
        cutoff_value = data.abs().median()
    elif cutoff == 'quantile':
        cutoff_value = data.abs().quantile(0.75)
    # Filter indexes based on condition
    filtered_indexes = data[data.abs() > cutoff_value].index
    return list(filtered_indexes)

def run_test(df, features, corr_matrix, model):
    results = {}
    # for action_feature in features:
    for action_feature in features:
        model_type = features[action_feature]['type']

        # Only keep features with strong correlation
        filtered_features = feature_keeper(corr_matrix, action_feature)

        X = df[filtered_features]
        filtered_feature_attributes = infer_feature_attributes(X)

        X = X.drop(columns=action_feature)
        y = df[action_feature]  # Target variable

        # Step 4: Split Data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        prediction = run_models(
            X_train=X_train,
            y_train=y_train,
            x_test=X_test,
            model=model,
            model_type=model_type,
            features=filtered_feature_attributes,
            action_feature=action_feature
        )

        if model_type == 'continuous':
            accuracy = mean_squared_error(y_test, prediction)
            print("MSE:", accuracy)
        else:
            accuracy = accuracy_score(y_test, prediction)
            print("Accuracy:", accuracy)

        results[action_feature] = accuracy

    return results

def mean_of_dictionaries(dict_list):
    # Check if the list is empty
    if not dict_list:
        return {}

    # Initialize a dictionary to store the sum of each key
    sum_dict = {key: 0 for key in dict_list[0].keys()}

    # Iterate over each dictionary
    for d in dict_list:
        # Add each value to the corresponding sum in sum_dict
        for key, value in d.items():
            sum_dict[key] += value

    # Calculate the mean for each key
    mean_dict = {key: value / len(dict_list) for key, value in sum_dict.items()}

    return mean_dict

def run_metric_full(datasets, df, matrices, model, metric, num_runs=3):
    dataset_results = {}
    for dataset in datasets:
        df = fetch_data(dataset, local_cache_dir=f"data/{dataset}")
        # Subsample the data to ensure the example runs quickly
        df = df.sample(3000)
        # Infer features attributes
        features = infer_feature_attributes(df)
        # matrices = get_matrices(df, features)
        for metric, matrix in matrices.items():
            if metric != metric:
                continue
            full_results = []
            for _ in range(num_runs):
                result = run_test(df, features, matrix, model)
                full_results.append(result)
            dataset_results[dataset] = full_results

    return dataset_results
