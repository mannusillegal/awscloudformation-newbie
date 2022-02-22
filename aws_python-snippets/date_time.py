# from datetime import datetime

# date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
# print(f"filename_{date}.html ")

from datetime import datetime, date, timedelta, timezone

today_date =  date.today()

yesterday = today_date - timedelta(days=1)
weekly = today_date - timedelta(weeks=7)

print(today_date)
print(yesterday)
print(weekly)

out = f"{weekly}:{yesterday}"
print(out)


