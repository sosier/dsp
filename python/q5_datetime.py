# Hint:  use Google to find python function

import datetime as dt

# a)
date_start = '01-02-2013'
date_stop = '07-28-2015'
dateFormat = "%m-%d-%Y"

start = dt.datetime.strptime(date_start, dateFormat)
stop = dt.datetime.strptime(date_stop, dateFormat)
print(stop - start)  # Prints 937 days

# b)
date_start = '12312013'
date_stop = '05282015'
dateFormat = "%m%d%Y"

start = dt.datetime.strptime(date_start, dateFormat)
stop = dt.datetime.strptime(date_stop, dateFormat)
print(stop - start)  # Prints 513 days

# c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
dateFormat = "%d-%b-%Y"

start = dt.datetime.strptime(date_start, dateFormat)
stop = dt.datetime.strptime(date_stop, dateFormat)
print(stop - start)  # Prints 7850 days
