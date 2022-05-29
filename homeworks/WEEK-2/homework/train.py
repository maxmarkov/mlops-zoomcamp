import argparse
import os
import pickle
import mlflow

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


def load_pickle(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


def run(data_path, mflow_tracking_uri, mlflow_expt_name, model_path):

    X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
    X_valid, y_valid = load_pickle(os.path.join(data_path, "valid.pkl"))
    
    mlflow.set_tracking_uri(mflow_tracking_uri)
    mlflow.set_experiment(mlflow_expt_name)

    mlflow.sklearn.autolog()

    with mlflow.start_run():
        rf = RandomForestRegressor(max_depth=10, random_state=0)

        with open(model_path, 'wb') as f_out:
            pickle.dump(rf, f_out)

        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_valid)

        mlflow.log_artifact(local_path=model_path, artifact_path="models_pickle")

        rmse = mean_squared_error(y_valid, y_pred, squared=False)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_path",
        default="./output",
        help="the location where the processed NYC taxi trip data was saved."
    )
    args = parser.parse_args()

    mlflow_tracking_uri = "sqlite:///db-mlflow/taxi.db"
    mlflow_expt_name = "nyc-taxi-experiment"
    model_path = 'homework/models/random_forest_reg.bin'
    
    run(args.data_path, mlflow_tracking_uri, mlflow_expt_name, model_path)
