def market_bias_engine(mmi_zone, rsi15, rsi60, pcr, vix):
    score = 0

    # ---- MMI ----
    z = mmi_zone.lower()
    if "fear" in z:
        score += 1
    elif "greed" in z:
        score -= 1

    # ---- RSI ----
    if rsi15 < 30 and rsi60 < 30:
        score += 1
    elif rsi15 < 30 and rsi60 < 40:
        score += 0.5
    elif rsi15 > 70 and rsi60 > 70:
        score -= 1
    elif rsi15 > 70 and rsi60 > 60:
        score -= 0.5

    # ---- PCR ----
    if pcr > 1.2:
        score += 1
    elif pcr < 0.8:
        score -= 1

    # ---- VIX (modifier) ----
    if vix < 12:
        score -= 0.5
    elif 18 <= vix <= 25:
        score += 0.25
    elif vix > 25:
        score -= 0.25

    # ---- Final Bias ----
    if score >= 1.5:
        bias = "Bullish"
        action = "Buy CE on dips"
    elif score >= 0.5:
        bias = "Mild Bullish"
        action = "Bull Put Spread"
    elif score <= -1.5:
        bias = "Bearish"
        action = "Sell PE on rallies"
    elif score <= -0.5:
        bias = "Mild Bearish"
        action = "Bear Call Spread"
    else:
        bias = "Neutral"
        action = "Sell strangle"

    # ---- VIX Overrides (Risk Control) ----
    if vix < 12:
        action = "Low VIX – Prefer spreads / No trade"

    if vix > 25 and "Buy" in action:
        action = "High VIX – Avoid naked buying"

    return round(score, 2), bias, action

