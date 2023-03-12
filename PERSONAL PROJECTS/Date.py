import datetime
import time
#NEW COMMENT
while True:
    try:
        years = int(input("enter the years:"))
        mounts = int(input("enter the mounts:"))
        days = int(input("enter the days:"))

    except:
        print("error")
        continue
    date = datetime.datetime(years,mounts,days)
    date_now = datetime.datetime.now()
    print(date)
    sleep = time.sleep(1.5)
    print(sleep)
    print(date.strftime("%A"))

    if date <= date_now:
        result = date_now-date
        print(result)
        week = result/7
        print("the week is ..."+str(week))
    elif date >= date_now:
        result = date-date_now
        print(result)
        week = result/7
        print("the week is ..."+str(week))
