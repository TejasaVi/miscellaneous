from flask import Blueprint, jsonify
from pnsea import NSE

PCR_INTERPRETATION = {
    "extreme_bullish": {
        "pcr_range": (0.0, 0.3),
        "sentiment": "Over-bullish",
		"action": "Buy ATM calls",
    },
    "bullish": {
        "pcr_range": (0.3, 0.7),
        "sentiment": "Bullish",
		"action": "Buy In the money calls"
    },
    "neutral": {
        "pcr_range": (0.7, 1.1),
        "sentiment": "Neutral",
		"action": "Rangebound wait for either side move."
    },
    "bearish": {
        "pcr_range": (1.1, 1.3),
        "sentiment": "Bearish",
		"action": "Buy near OTM Calls with strict SL"
    },
    "extreme_bearish": {
        "pcr_range": (1.3, float("inf")),
        "sentiment": "Extreme bearish",
		"action": "Buy ATM Puts at nearest resistance",
    }
}


def get_pcr_sentiment(pcr_value):
    """
    Returns sentiment classification for a given PCR value
    """
    for zone, info in PCR_INTERPRETATION.items():
        low, high = info["pcr_range"]
        if low <= pcr_value < high:
            return {
                "zone": zone,
                "sentiment": info["sentiment"],
				"action": info["action"]
            }

    return {
        "zone": "unknown",
        "sentiment": "Unknown",
		"action": "unknown"
    }

def get_current_expiry_pcr():
    nse = NSE()
    df = nse.options.option_chain("NIFTY")[0]
    pcr = df['PE_openInterest'].sum() / df['CE_openInterest'].sum()
    pcr_sentiment = get_pcr_sentiment(pcr)
    pcr_sentiment['pcr'] = pcr
    return {
            "pcr": pcr,
			"sentiment": pcr_sentiment["sentiment"],
			"action": pcr_sentiment["action"],
            }

    raise RuntimeError("PCR could not be calculated")

pcr_bp = Blueprint("pcr", __name__)

@pcr_bp.route("/pcr", methods=["GET"])
def pcr_check():
    pcr = get_current_expiry_pcr()
    print(pcr)
    return jsonify(pcr)
