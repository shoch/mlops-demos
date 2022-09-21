# mlops-demo

simple demos for different mlops tools

* [DVC](dvc)
* [MLFlow](mlflow/README.md)
* [Weights&Biases](wandb)


## MLFlow
### Experiment Tracking:

```python
# Automatic logging with mlflow

mlflow.tensorflow.autolog()

with mlflow.start_run():
  ...
```

```python
# Manuel logging with mlflow

# Start a run
mlflow.start_run()
# Log an hyper-param
mlflow.log_param()
# Log a metric
mlflow.log_metric()
```






# Contribution
## Pre-commit hooks
This project provides pre-commit hooks for developers. Run 'pre-commit install' to setup git hook scripts. In case you actively want to ignore all hooks, use git commit --no-verify.
* pre-commit run --all-files

## Testing

* pytest don't can handle marks on fixtures
* cd [project]
* pytest -m "not integtest"
* pytest -m integtest
