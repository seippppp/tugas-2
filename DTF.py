HH, MM, SS = map(int, input().split(":"))
CH, CM, CS = map(int, input().split(":"))

HH = HH + 5

stream_time = HH * 3600 + MM * 60 + SS
now_time = CH * 3600 + CM * 60 + CS

diff = stream_time - now_time
if diff < 0:
    print("see you on the next pear event")
else:
    hours = diff // 3600
    diff % 3600
    minute = diff // 60
    second = diff % 60
    print(f"{hours:02}:{minute:02}:{second:02}")