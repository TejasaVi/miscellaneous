from flask import Blueprint, jsonify

from app.api.vix import get_india_vix
from app.api.mmi import fetch_mmi
from app.api.pcr import get_current_expiry_pcr
from app.api.rsi import get_nifty_rsi
from app.services.market_bias import market_bias_engine


def define_market_bias():
    # ---- Fetch inputs ----
    vix = get_india_vix()
    vix = vix["value"]
    print(vix)
    mmi_zone = fetch_mmi()
    mmi_zone = mmi_zone["zone"]
    print(mmi_zone)
    pcr = get_current_expiry_pcr()
    pcr = pcr["pcr"]
    print(pcr)

    rsi60_data = get_nifty_rsi(interval="60m")
    rsi15_data = get_nifty_rsi(interval="15m")

    rsi60 = float(rsi60_data["rsi_value"].iloc[0])
    rsi15 = float(rsi15_data["rsi_value"].iloc[0])

    print(rsi60, rsi15)
    # ---- Bias Engine ----
    score, bias, action = market_bias_engine(
        mmi_zone, rsi15=rsi15, rsi60=rsi60, pcr=pcr, vix=vix
    )

    return jsonify(
        {
            "bias": bias,
            "action": action,
            "score": score,
            "vix": round(vix, 2),
            "inputs": {
                "mmi_zone": mmi_zone,
                "rsi15": round(rsi15, 2),
                "rsi60": round(rsi60, 2),
                "pcr": round(pcr, 2),
            },
        }
    )


marketbias_bp = Blueprint("market_bias", __name__)


@marketbias_bp.route("/marketbias", methods=["GET"])
def bias_check():
    return define_market_bias()
    return {}
