from datetime import datetime

i = 0
squad = []
number_of_squads = 1

with open('document.txt', 'r') as file:
    timeframe = file.readline().strip()
    lines = file.readlines()
    for line in lines:
        if line.strip() == '':
            number_of_squads += 1
        else:
            squad.append(line)

print(squad) 
    # number_of_squads = sum(1 for line in lines if line.strip() == '') + 1

start_time, end_time = timeframe.split(" - ")

start_hour, start_minute = map(int, start_time.split(":"))
end_hour, end_minute = map(int, end_time.split(":"))

if start_hour > end_hour:
    time_length = 60 * (24 - start_hour) - start_minute + 60 * end_hour + end_minute
# elif:
    


print(time_length)
print(number_of_squads)
print(end_time)


    




