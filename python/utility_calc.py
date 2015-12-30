#!/usr/bin/python
"""
"""
#################################################################
# Function to calculate the appriciated price and appriciation  #
#################################################################
def get_price(cur_price, percent):
    fut_price = cur_price
    appriciation = float(percent)/100 * float(cur_price)
    fut_price = fut_price + int(appriciation)
    appriciation_f = (int((appriciation - int(appriciation)) * 100) -
                      int((appriciation - int(appriciation)) * 100) % 5) * 0.01
    appriciation = float(int(appriciation) + appriciation_f)
    fut_price = fut_price + appriciation_f
    return fut_price, appriciation


################################################################
# Function to calculate the series of upper curciuts a script  #
################################################################
def get_series(count, cur_price, percent):
    fut_price = []
    for i in xrange(0, count):
        price, _ = get_price(cur_price, percent)
        fut_price.append(round(price, 2))
        cur_price = price
    return fut_price


##########################################################
# Function to calculate returns percentage from a script #
##########################################################
def returns_percentage(buy_price, sell_price, dividend=0):
    if dividend:
        buy_price = buy_price + dividend
    if ((buy_price and buy_price >0) and (sell_price and sell_price >0)):
        # differnce can be positive/negative
        differnce = sell_price - buy_price
        ret_percent = (differnce/buy_price) * 100
        return round(ret_percent,2)
    return None


#######################################################
# Function to calculate profit/loss in currency units #
#######################################################
def returns(buy_price, sell_price, dividend=0):
    if dividend:
        buy_price = buy_price + dividend
    if ((buy_price and buy_price >0) and (sell_price and sell_price >0)):
        differnce = sell_price - buy_price
        if(differnce > -1):
            returns_state = 'profit'
        else:
            returns_state = 'loss'
        return differnce, returns_state
    return None,'Incorrect inputs'


##################################################
# Function to calculate dividend amount in units #
##################################################
def get_dividend(base_price,dividend,equity=1):
    if equity > 1:
        return base_price * dividend *0.01 * equity
    else:
        return base_price * dividend *0.01


################################################################
# Function to find number of shares in investment for a script #
################################################################
def get_equity(cur_price, total_amt):
    total_equity = total_amt / cur_price
    return int(total_equity)


###########################################
# Function to find investment in a script #
###########################################
def get_investment(cur_price, total_shrs):
    total_inv = float(total_shrs) * cur_price
    return total_inv
###########################################################

if __name__ == '__main__':
    # inputs from the User.
    #limit = int(raw_input('Enter Upper Curcuit Limit(in percentage%): '))
    cur_price = float(raw_input('Enter Current Share Price: '))
    inv_amt = float(raw_input('Enter Amount for investment: '))
    # buy = float(raw_input('Enter Buy Price: '))
    # sell = float(raw_input('Enter Sell Price: '))
    total_equity = get_equity(cur_price, inv_amt)
    print total_equity
    """
    price, app = get_price(cur_price, limit)
    print "Price: {} and Appriciation: {}".format(price, app)
    series = get_series(10,cur_price, limit)
    print series
    ret = returns_percentage(buy, sell)
    print "Returns : {} %".format(ret)
    ret, state = returns(buy, sell)
    print "Returns: {0} with state: {1}".format(ret, state)
    div = get_dividend(cur_price,30,100)
    print div
    """
