import pickle
import numpy as np

# load trained model
model = pickle.load(open("model.pkl", "rb"))

def handler(request):

    data = request.json()

    open_price = float(data["Open"])
    high_price = float(data["High"])
    low_price = float(data["Low"])
    volume = float(data["Volume"])

    features = np.array([[open_price, high_price, low_price, volume]])

    prediction = model.predict(features)[0]

    # simple buy/sell logic
    decision = "BUY" if prediction > open_price else "SELL"

    return {
        "prediction": float(prediction),
        "decision": decision
    }
