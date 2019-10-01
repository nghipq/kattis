import datetime

temp = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
inp = list(map(int, input().split()))

try:
    print(temp.get(datetime.date(2009, inp[1], inp[0]).weekday()))
except:
    pass