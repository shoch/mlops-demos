from surprise import Dataset, Reader
from surprise.model_selection import PredefinedKFold


class DataLoader:
    def __init__(self) -> None:
        path_train_data = "../data/ml-100k/u1.base"
        path_test_data = "../data/ml-100k/u1.test"
        reader = Reader(line_format="user item rating timestamp", sep="\t")
        self.data = Dataset.load_from_folds(
            [
                (path_train_data, path_test_data),
            ],
            reader=reader,
        )

    def get_data(self):
        trainset, testset = next(PredefinedKFold().split(self.data))
        return trainset, testset
