import datetime

# notice 
# 1. year is 1xx6
# 2. feb has 29 days
# 3. 1-26 is monday

# the first leap year is 1016

lst = []

for i in range(1016, 2019, 20):
    x = datetime.datetime(i, 1, 26)
    if x.strftime("%w") == "1":
        lst = lst + [x.strftime("%Y")]
    
print(lst[-2], end="")
print("-01-26")

# search on google
# Born on 1756-01-26