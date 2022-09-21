# MLFlow
* [MLflow docu ](https://mlflow.org/) an open source platform for the machine learning lifecycle.
* [Demo](#0-prerequisites) Experiment Tracking and Model Registry.
* [More examples.](https://github.com/mlflow/mlflow/tree/master/examples)



# Demo
### Prerequisites
* Load Data
  * Download movielens 100k from https://grouplens.org/datasets/movielens/100k/
  * unpack to ./data/ml-100k

### Setup Enviorment
* MLflow
  * conda create --name mlflow-demo python=3.9
  * conda activate mlflow-demo
  * pip install -r requirements-mlflow.txt
* MLflow-Server
  * Model-Registry needs SQL backend
  * mlflow server --backend-store-uri sqlite:///C:\Users\sebih\Documents\mlops-demos\data\mlflow-database\mlruns.db --default-artifact-root file///C:\Users\sebih\Documents\mlops-demos\data\mlflow-runs
