import pickle
import numpy as np

# load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

def handler(request):

    data = request.json()

    open_price = float(data["open"])
    high = float(data["high"])
    low = float(data["low"])
    volume = float(data["volume"])

    features = np.array([[open_price, high, low, volume]])

    # scale input
    scaled_features = scaler.transform(features)

    prediction = model.predict(scaled_features)[0]

    decision = "BUY" if prediction > open_price else "SELL"

    return {
        "prediction": float(prediction),
        "decision": decision
    }
