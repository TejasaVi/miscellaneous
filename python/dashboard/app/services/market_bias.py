import json

def option_signal_engine(mmi, rsi15, rsi60, pcr, vix, spot, expiry_type="WEEKLY"):
    """
    Returns a JSON with:
    - score (0-100)
    - bias (Bullish/Bearish/Neutral)
    - primary_action
    - strategy_list
    - strikes for CE, PE, spreads, Iron Condor, Butterfly, Calendar
    - warnings
    """

    # --- Step 1: Calculate Bias Score ---
    score = 50  # neutral baseline

    # MMI
    if "Extreme Fear" in mmi:
        score += 20
    elif "Fear" in mmi:
        score += 10
    elif "Greed" in mmi:
        score -= 10
    elif "Extreme Greed" in mmi:
        score -= 20

    # RSI
    if isinstance(rsi15, (int, float)) and isinstance(rsi60, (int, float)):
        if rsi15 < 30 and rsi60 < 40:
            score += 15
        elif rsi15 > 70 and rsi60 > 60:
            score -= 15

    # PCR
    if isinstance(pcr, (int, float)):
        if pcr < 0.7:
            score -= 15
        elif pcr > 1.3:
            score += 15

    # VIX
    if isinstance(vix, (int, float)):
        if vix < 14:
            score += 10
        elif vix > 18:
            score -= 10

    # Clamp
    score = max(0, min(score, 100))

    # --- Step 2: Determine Bias & Primary Action ---
    if score >= 65:
        bias = "Bullish"
        primary_action = "Buy Calls / Bullish Spread"
        strategy_list = [
            "Bull Call Spread", "Bull Put Spread", "Long Straddle",
            "Long Strangle", "Iron Condor", "Butterfly Spread", "Calendar Spread"
        ]
    elif score <= 35:
        bias = "Bearish"
        primary_action = "Buy Puts / Bearish Spread"
        strategy_list = [
            "Bear Put Spread", "Bear Call Spread", "Long Straddle",
            "Long Strangle", "Iron Condor", "Butterfly Spread", "Calendar Spread"
        ]
    else:
        bias = "Neutral"
        primary_action = "Long Straddle / Long Strangle"
        strategy_list = [
            "Long Straddle", "Long Strangle", "Iron Condor", "Butterfly Spread", "Calendar Spread"
        ]

    # --- Step 3: Determine base distance for strikes ---
    if vix < 12:
        base = 50 if expiry_type == "WEEKLY" else 100
    elif vix < 16:
        base = 100 if expiry_type == "WEEKLY" else 150
    elif vix < 20:
        base = 150 if expiry_type == "WEEKLY" else 250
    else:
        base = 250 if expiry_type == "WEEKLY" else 400

    # Round spot to nearest 50 for ATM
    atm = round(spot / 50) * 50

    # --- Step 4: Populate Strikes ---
    strikes = {
        "ce_strike": atm,
        "pe_strike": atm,
        "spread_ce": {"buy": None, "sell": None},
        "spread_pe": {"buy": None, "sell": None},
        "iron_condor": {"sell_ce": None, "buy_ce": None, "sell_pe": None, "buy_pe": None},
        "butterfly": {"buy_lower": None, "sell": None, "buy_upper": None},
        "calendar": {"ce_atm": None, "pe_atm": None},
        "warnings": []
    }

    # --- Single Leg CE/PE ---
    strikes["ce_strike"] = atm + base if "Bull" in bias else atm
    strikes["pe_strike"] = atm - base if "Bear" in bias else atm

    # --- Bull/Bear Spreads ---
    if "Bull" in bias:
        strikes["spread_ce"] = {"buy": atm, "sell": atm + base}
        strikes["spread_pe"] = {"buy": atm - base, "sell": atm}
    elif "Bear" in bias:
        strikes["spread_ce"] = {"buy": atm, "sell": atm + base}
        strikes["spread_pe"] = {"buy": atm - base, "sell": atm}

    # --- Iron Condor ---
    strikes["iron_condor"] = {
        "sell_ce": atm + base,
        "buy_ce": atm + 2*base,
        "sell_pe": atm - base,
        "buy_pe": atm - 2*base
    }

    # --- Butterfly Spread ---
    strikes["butterfly"] = {
        "buy_lower": atm - base,
        "sell": atm,
        "buy_upper": atm + base
    }

    # --- Calendar Spread (simplified as ATM CE/PE) ---
    strikes["calendar"] = {
        "ce_atm": atm,
        "pe_atm": atm
    }

    # --- Strangle / Straddle warnings ---
    if vix < 12:
        strikes["warnings"].append("⚠️ Low VIX: Premiums are cheap, selling may underperform")
    if vix > 20:
        strikes["warnings"].append("⚠️ High VIX: Expect wild swings & large premiums")
    if expiry_type == "WEEKLY":
        strikes["warnings"].append("⏰ Weekly expiry: Fast theta decay")

    # --- Step 5: Return JSON-ready dictionary ---
    return {
        "score": score,
        "bias": bias,
        "primary_action": primary_action,
        "strategy_list": strategy_list,
        "strikes": strikes,
        "vix": vix
    }

