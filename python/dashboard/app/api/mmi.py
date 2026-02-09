from flask import Blueprint, jsonify
from tickersnap.mmi import MarketMoodIndex


def mmi_action(zone):
    """
    Returns actionable market suggestion based on MMI zone
    """
    zone = zone.lower()

    if "extreme fear" in zone:
        return {
            "bias": "Bullish (Reversal)",
            "action": "Accumulate longs slowly, prefer spreads",
            "strategies": [
                "Bull Put Spread",
                "Call Calendar",
                "Deep ITM Calls (small size)"
            ]
        }

    elif "fear" in zone:
        return {
            "bias": "Bullish",
            "action": "Buy on dips, avoid aggressive shorts",
            "strategies": [
                "Bull Call Spread",
                "Ratio Call Spread"
            ]
        }

    elif "neutral" in zone:
        return {
            "bias": "Sideways",
            "action": "Sell premium or trade range",
            "strategies": [
                "Iron Condor",
                "Calendar Spread",
                "Short Strangle (hedged)"
            ]
        }

    elif "greed" in zone and "extreme" not in zone:
        return {
            "bias": "Bullish (Late trend)",
            "action": "Ride trend with caution, tighten stop-loss",
            "strategies": [
                "Call Spread",
                "Buy Calls on pullback"
            ]
        }

    elif "extreme greed" in zone:
        return {
            "bias": "Cautious / Bearish",
            "action": "Book profits, hedge longs, avoid fresh buying",
            "strategies": [
                "Bear Call Spread",
                "Put Calendar",
                "Protective Puts"
            ]
        }

    return {
        "bias": "Unknown",
        "action": "Stay cautious",
        "strategies": []
    }


def fetch_mmi():
    mmi = MarketMoodIndex()
    current = mmi.get_current_mmi()

    action_info = mmi_action(current.zone.value)

    return {
        "value": current.value,
        "zone": current.zone.value,
        "bias": action_info["bias"],
        "action": action_info["action"],
        "preferred_strategies": action_info["strategies"]
    }


mmi_bp = Blueprint("mmi", __name__)


@mmi_bp.route("/mmi", methods=["GET"])
def mmi_check():
    return jsonify(fetch_mmi())
