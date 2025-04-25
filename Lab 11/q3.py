import pandas as pd

asking_prices = pd.Series([15000, 20000, 18000, 12000, 25000])
fair_prices = pd.Series([16000, 19000, 19000, 13000, 24000])

good_deals = asking_prices < fair_prices
good_deals_indices = good_deals[good_deals].index.tolist()

print(good_deals_indices)