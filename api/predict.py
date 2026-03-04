import pickle
import json
import numpy as np

# load model
model = pickle.load(open("model.pkl","rb"))

def handler(request):

    data = request.json()

    features = np.array([[
        float(data["feature1"]),
        float(data["feature2"]),
        float(data["feature3"]),
        float(data["feature4"])
    ]])

    prediction = model.predict(features)[0]

    decision = "BUY" if prediction > 0 else "SELL"

    return {
        "prediction": float(prediction),
        "decision": decision
    }
