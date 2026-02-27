#1
import datetime
x = datetime.datetime.now()
new_date=x-datetime.timedelta(days=5)
print(new_date)

#2
import datetime
x=datetime.datetime.now()
print(x - datetime.timedelta(days=1))
print(x)
print(x + datetime.timedelta(days=1))

#3
import datetime
x = datetime.datetime.now()
print(x.replace(microsecond=0))

#4
import datetime
d1 = datetime.datetime(2026, 1, 1, 12, 0, 0)
d2 = datetime.datetime(2026, 1, 2, 12, 0, 0)
diff = d2 - d1
print(int(diff.total_seconds()))

