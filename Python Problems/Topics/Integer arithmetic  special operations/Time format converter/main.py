

if hour == 0:
    print(12)
elif hour <= 11:
    print(hour)
elif hour == 12:
    print(12)
elif hour >=13 and hour <= 23:
    num = hour % 12
    print(num)