import datetime as DT

text = str(DT.datetime.now())

#date = DT.datetime.strptime(text, '%Y%m%d').date()
#print(date)                       # 2018-08-19
#print(str(date))                  # 2018-08-19
#print(date.strftime('%Y-%m-%d'))  # 2018-08-19




print(type(text))