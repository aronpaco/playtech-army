from datetime import datetime

with open('document.txt', 'r') as file:
    timeframe = file.readline().strip()

start_time, end_time = timeframe.split(" - ")

start_hour, start_minute = map(int, start_time.split(":"))
end_hour, end_minute = map(int, end_time.split(":"))

if start_hour > end_hour:
    time_length = 24 - start_hour + end_hour

print(time_length)
print(start_hour, start_minute)
print(end_time)


    




