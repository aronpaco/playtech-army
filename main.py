from datetime import datetime

squad = []
squads = []
arranged_squad = []
arranged_squads = []
number_of_squads = 1

with open('document.txt', 'r') as file:
    timeframe = file.readline().strip()
    lines = file.readlines()
    for line in lines:
        line = line.replace('\n', '')
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
    
for squad in squads:
    number_of_members_per_squad = len(squad)
    patrol_length_per_squad = time_length / number_of_squads
    patrol_length_per_duo = patrol_length_per_squad / number_of_members_per_squad * 2

    if time_length <= 60 * 6:
        print("Drivers will not have any duties")
    elif time_length - patrol_length_per_duo < 60 * 6:
        print("Drivers will not do a full length of patrol; the patrol_length_per_duo must be recalculated")
    else:
        for soldier in squad:
            if soldier.find("(Driver)") != -1:
                arranged_squad.append(soldier)
        for soldier in squad:
            if soldier.find("(Driver)") == -1:
                arranged_squad.append(soldier)
        arranged_squads.append(arranged_squad)
        arranged_squad = []

print(arranged_squads)


    




