from datetime import date, timedelta

today = date.today()
print(today)

f_day = today.strftime("%a %d-%b-%Y")
print(f_day)

date_after_65_days = today + timedelta(days=65)
print(date_after_65_days)

# 2025-01-15 1995-09-06

# days, weeks, months

diff = date(2025, 1, 15) - date(1995, 9, 6)


d0 = date(2025, 1, 15)
d1 = date(1995, 9, 6)
delta = d1 - d0
print(delta.days)


print(diff.days)


# pip install pillow

