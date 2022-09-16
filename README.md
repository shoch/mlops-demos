# mlops-demo

simple demos for different mlops tools


# DVC

[DVC docu](https://dvc.org/)

Dataversioning

```
dvc add ...
dvc remote add -d myremote ...

dvc push

dvc pull
```

# MLFlow
[MLflow](https://mlflow.org/) an open source platform for the machine learning lifecycle.

[Demo](./mlflow/): Experiment Tracking and Model Registry.
[More examples.](https://github.com/mlflow/mlflow/tree/master/examples)

Experiment Tracking:

```python
# Manuel logging with mlflow

# Start a run
mlflow.start_run()
# Log an hyper-param
mlflow.log_param()
# Log a metric
mlflow.log_metric()
```

```python
# Automatic logging with mlflow

mlflow.tensorflow.autolog()

with mlflow.start_run():
  ...
```


### Prerequisites
* Load Data
  * Download movielens 100k from https://grouplens.org/datasets/movielens/100k/
  * unpack to ./data/ml-100k

### Enviorment
* MLflow
  * conda create --name mlflow-demo python=3.9
  * conda activate mlflow-demo
  * pip install -r requirements-mlflow.txt
* MLflow-Server
  * Model-Registry needs SQL backend
  * mlflow server --backend-store-uri sqlite:///C:\Users\sebih\Documents\mlops-demos\data\mlflow-database\mlruns.db --default-artifact-root file///C:\Users\sebih\Documents\mlops-demos\data\mlflow-runs

# Wheights& Biases
[Wheights& Biases](https://wandb.ai/site) Experiment Tracking
[Demo](wandb)




# Contribution
## Pre-commit hooks
This project provides pre-commit hooks for developers. Run 'pre-commit install' to setup git hook scripts. In case you actively want to ignore all hooks, use git commit --no-verify.
* pre-commit run --all-files

## Testing
* todo
* pytest don't can handle marks on fixtures
* cd [project]
* pytest -m "not integtest"
* pytest -m integtest
* pytest -m "not slow"
