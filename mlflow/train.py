# python train.py --n_epochs 25 --lr_all 0.005

import argparse

from data_loader import DataLoader
from evaluation import Evaluation
from surprise import SVDpp

import mlflow

# optional set tracking uri to remote
remote_server_uri = "http://127.0.0.1:5000/"  # set to your server URI
mlflow.set_tracking_uri(remote_server_uri)

# hyperparameter
parser = argparse.ArgumentParser()

parser.add_argument("--n_epochs", type=int, default=25)
parser.add_argument("--lr_all", type=float, default=0.005)
args = parser.parse_args()

n_epochs = args.n_epochs
lr_all = args.lr_all

trainset, testset = DataLoader().get_data()

EXPERIMENT_NAME = "RecSys_MovieLens"

experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
if experiment is None:
    experiment_id = mlflow.create_experiment(EXPERIMENT_NAME)
    experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)

mlflow.start_run(experiment_id=experiment.experiment_id, run_name="SVDpp")
mlflow.log_param("n_epochs", n_epochs)
mlflow.log_param("lr_all", lr_all)

algo = SVDpp(n_epochs=n_epochs, lr_all=lr_all)
mlflow.set_tag("algorithm", type(algo))

algo.fit(trainset)

# evaluation
predictions = algo.test(testset)
results = Evaluation().evaluate(predictions)

mlflow.log_metrics(
    metrics={
        "RMSE": results["rmse"],
        "Recall_10": results["recall@10"],
        "Precision_10": results["precision@10"],
    },
)


# Define the model class
class PackedSurprise(mlflow.pyfunc.PythonModel):
    def __init__(self, algo):
        self.n = algo

    def predict(self, context, model_input):
        return algo.predict(uid=model_input["uid"], iid=model_input["iid"])


packed_model = PackedSurprise(algo)

mlflow.pyfunc.log_model(
    artifact_path="SVDpp",
    python_model=packed_model,
)

mlflow.end_run()
