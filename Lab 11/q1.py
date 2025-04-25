import pandas as pd

date_time_a = pd.to_datetime("2012-01-15")
print(date_time_a)

date_time_b = pd.to_datetime("2012-01-15 21:20")
print(date_time_b)

local_date_time = pd.to_datetime("now")
print(local_date_time)

date_without_time = pd.to_datetime("2012-01-15").date()
print(date_without_time)

current_date = pd.to_datetime("today").date()
print(current_date)

time_from_date = date_time_b.time()
print(time_from_date)

current_local_time = pd.to_datetime("now").time()
print(current_local_time)