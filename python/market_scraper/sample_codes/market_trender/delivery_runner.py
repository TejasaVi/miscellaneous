import pprint as pprint
from deliveryData import StockDeliveryData as delivery
from deliveryData import FNOData as fno

#today = delivery("14122022")
#pprint.pprint(today.parse_data(turnover=100, last_price=4000))

print("="*80)
fno_data = fno()
pprint.pprint(fno_data.get_fno_stocks_with_delivery_percentage(date="15122022", percentage=60))
