from datetime import timedelta, datetime
 
 
dada = '2021-01-27 00:59:38.057917'

dada = datetime.date(dada)
now = datetime.now()
print(now)                      # 2017-05-03 17:46:44.558754
two_days = timedelta(365)
in_two_days = now - two_days
print(in_two_days)


print(type(now))

print(now-two_days)


if now > now+two_days :
    print('ok')