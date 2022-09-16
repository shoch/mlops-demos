# flask --app app run  --port=6000
# insomnia post http://127.0.0.1:6000/calc_score/user=1/item=2
from flask import Flask, jsonify

import mlflow

app = Flask(__name__)


def load_model(model_name="RecSys", stage="Production"):
    remote_server_uri = "http://127.0.0.1:5000/"
    mlflow.set_tracking_uri(remote_server_uri)
    return mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{stage}")


model = load_model()


@app.route("/calc_score/user=<user>/item=<item>", methods=["POST"])
def calc_score_by(user, item):

    # datapreparation
    # e.x. userId -> uiid; itemId to iid
    data = {"uid": user, "iid": item}

    res = model.predict(data)

    return jsonify(res.est)
