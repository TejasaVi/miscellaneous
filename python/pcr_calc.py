from nsepy import get_history
from datetime import date

def get_oi_sum(st_range, ed_range, opt_type='CE', index=50):
    tmp_indx = st_range
    total_oi_sum = 0
    while(tmp_indx<=ed_range):
        nifty_opt = get_history(symbol="NIFTY",start=date(2018,6,1), end=date(2018,6,7), index=True, option_type=opt_type, strike_price=tmp_indx, expiry_date=date(2018,6,28))
        nifty_opt_data = nifty_opt.to_dict()
        oi_for_day = nifty_opt_data['Open Interest'].items()[0][1]
        total_oi_sum = total_oi_sum + oi_for_day
        tmp_indx = tmp_indx + index
        print oi_for_day
    return total_oi_sum

pcr = float(get_oi_sum(10000,11000,opt_type='PE',index=100))/get_oi_sum(10000,11000, index=100)
#pcr = float(get_oi_sum(10900,10900,opt_type='PE',index=100))/get_oi_sum(10900,10900, index=100)
print pcr
