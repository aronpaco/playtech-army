from datetime import datetime

i = 0
squad = []
squads = []
number_of_squads = 1

with open('document.txt', 'r') as file:
    timeframe = file.readline().strip()
    lines = file.readlines()
    for line in lines:
        if line.strip() == '':
            number_of_squads += 1
            squads.append(squad)
            squad = []
        else:
            squad.append(line)
    squads.append(squad)

print(squads) 

start_time, end_time = timeframe.split(" - ")

start_hour, start_minute = map(int, start_time.split(":"))
end_hour, end_minute = map(int, end_time.split(":"))

if start_hour > end_hour:
    time_length = 60 * (24 - start_hour) - start_minute + 60 * end_hour + end_minute
# elif:
    


    




