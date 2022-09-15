# mlflow-demo

## PrePrerequisites
* Load Data
  * Download movielens 100k from https://grouplens.org/datasets/movielens/100k/
  * unpack to ./data/ml-100k

## Enviorment
* MLflow
  * conda create --name mlflow-demo python=3.9
  * conda activate mlflow-demo
  * pip install -r requirements-mlflow.txt
* MLflow-Server
  * Model-Registry needs SQL backend
  * mlflow server --backend-store-uri sqlite:///C:\Users\sebih\Documents\mlflow-demo\data\mlflow-database\mlruns.db --default-artifact-root file///C:\Users\sebih\Documents\mlflow-demo\data\mlflow-runs


# Contribution
## Pre-commit hooks
This project provides pre-commit hooks for developers. Run 'pre-commit install' to setup git hook scripts. In case you actively want to ignore all hooks, use git commit --no-verify.
pre-commit run --all-files

## Testing

cd <project>
pytest -m "not integtest"
pytest -m integtest
pytest -m "not slow"
pytest don't can handle marks on fixtures
