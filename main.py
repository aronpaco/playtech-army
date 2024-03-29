from datetime import datetime

i = 0
squad = []
squads = []
number_of_squads = 1
member_count = 0

with open('document.txt', 'r') as file:
    timeframe = file.readline().strip()
    lines = file.readlines()
    last = lines[-1]
    for line in lines:
        if line.strip() == '' or line is last:
            if member_count < 5:
                print("WARNING: Squad contains less than 5 people")
            elif member_count > 12:
                print("WARNING: Squad contains more than 12 people")
            member_count = 0
            number_of_squads += 1
            squads.append(squad)
            squad = []
        else:
            member_count += 1
            squad.append(line)

start_time, end_time = timeframe.split(" - ")
start_hour, start_minute = map(int, start_time.split(":"))
end_hour, end_minute = map(int, end_time.split(":"))

if start_hour > end_hour:
    time_length = 60 * (24 - start_hour) - start_minute + 60 * end_hour + end_minute
# elif:
    



print(squads)
print(time_length)
print(number_of_squads)
print(end_time)


    




