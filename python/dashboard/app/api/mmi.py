from flask import Blueprint, jsonify
from tickersnap.mmi import MarketMoodIndex


def fetch_mmi():
	mmi = MarketMoodIndex()
	current = mmi.get_current_mmi()
	return {
		"value": current.value,
		"zone": current.zone.value
		}

mmi_bp = Blueprint("mmi", __name__)


@mmi_bp.route("/mmi", methods=["GET"])
def mmi_check():
    mmi = fetch_mmi()

    return mmi

