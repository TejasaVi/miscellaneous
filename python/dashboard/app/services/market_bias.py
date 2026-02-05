def market_bias_engine(mmi, rsi15, rsi60, pcr, vix):
    score = 50  # 🔑 neutral baseline

    # --- MMI ---
    if "Extreme Fear" in mmi:
        score += 20
    elif "Fear" in mmi:
        score += 10
    elif "Greed" in mmi:
        score -= 10
    elif "Extreme Greed" in mmi:
        score -= 20

    # --- RSI ---
    if rsi15 < 30 and rsi60 < 40:
        score += 15
    elif rsi15 > 70 and rsi60 > 60:
        score -= 15

    # --- PCR ---
    if pcr < 0.7:
        score -= 15
    elif pcr > 1.3:
        score += 15

    # --- VIX ---
    if vix < 14:
        score += 10
    elif vix > 18:
        score -= 10

    # --- Clamp ---
    score = max(0, min(score, 100))

    # --- Decision ---
    if score >= 65:
        bias = "Bullish"
        action = "Buy CE on dips"
    elif score <= 35:
        bias = "Bearish"
        action = "Sell rallies / Buy PE"
    else:
        bias = "Neutral"
        action = "Sell strangle"

    return score, bias, action


def suggest_option_strikes(
    spot: float,
    bias: str,
    action: str,
    vix: float,
    expiry_type: str = "WEEKLY",  # WEEKLY or MONTHLY
):
    """
    Returns CE/PE strike suggestions with warnings
    """

    # --- Step 1: Determine base distance ---
    if vix < 12:
        base = 50 if expiry_type == "WEEKLY" else 100
    elif vix < 16:
        base = 100 if expiry_type == "WEEKLY" else 150
    elif vix < 20:
        base = 150 if expiry_type == "WEEKLY" else 250
    else:
        base = 250 if expiry_type == "WEEKLY" else 400

    # Round spot to nearest 50
    atm = round(spot / 50) * 50

    result = {
        "atm": atm,
        "ce_strike": None,
        "pe_strike": None,
        "distance": base,
        "warnings": [],
    }

    # --- Step 2: Strategy based strikes ---
    action = action.lower()

    if "buy ce" in action:
        result["ce_strike"] = atm + base

    elif "buy pe" in action:
        result["pe_strike"] = atm - base

    elif "sell ce" in action:
        result["ce_strike"] = atm + base

    elif "sell pe" in action:
        result["pe_strike"] = atm - base

    elif "strangle" in action:
        result["ce_strike"] = atm + base
        result["pe_strike"] = atm - base

    elif "straddle" in action:
        result["ce_strike"] = atm
        result["pe_strike"] = atm

    # --- Step 3: Warnings ---
    if vix < 12 and "sell" in action:
        result["warnings"].append(
            "⚠️ Low VIX: Premiums are cheap, selling may underperform"
        )

    if vix > 20:
        result["warnings"].append("⚠️ High VIX: Expect wild swings & large premiums")

    if expiry_type == "WEEKLY":
        result["warnings"].append("⏰ Weekly expiry: Fast theta decay")

    return result
