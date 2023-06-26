from yahoo_fin.stock_info import get_data

msft = get_data("MSFT", start_date="09/17/2021", end_date="09/30/2021", index_as_date = True, interval="1d")
print(msft)
