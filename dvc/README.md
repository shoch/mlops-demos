
# DVC

[DVC docu](https://dvc.org/)

Dataversioning

```
dvc add ...
dvc remote add -d myremote ...

dvc push

dvc pull
```

# MLFlow Demo
### Prerequisites
* [init dvc in 'your' remote](https://dvc.org/doc/start)
  * dvc init
  * git commit -m "Initialize DVC"
  * dvc add data/ml-100k
  * git commit -m "Add data"
  * dvc remote add -d mylocalremote [C:\Users\sebih\Documents\data\ml-ops-demo](https://dvc.org/doc/command-reference/remote/add#supported-storage-types)
  * dvc push
  * git add ..., git commit ..., git push ...
  * [dvc pull](https://dvc.org/doc/start/data-management/data-versioning#retrieving)
