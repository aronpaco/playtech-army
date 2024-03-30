squad = []
squads = []
arranged_squad = []
arranged_squads = []
patrol_shifts = []
stove_shifts = []
number_of_squads = 1
number_of_drivers = 0

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

# print(squads)

start_time, end_time = timeframe.split(" - ")
start_hour, start_minute = map(int, start_time.split(":"))
end_hour, end_minute = map(int, end_time.split(":"))
start_time_in_minutes = start_hour * 60 + start_minute
end_time_in_minutes = end_hour * 60 + end_minute

if start_hour > end_hour:
    time_length = 24 * 60 - start_time_in_minutes + end_time_in_minutes
    print(start_time_in_minutes)
# elif:
    
def convert_time_in_minutes_to_formatted_time(time_in_minutes):
    if time_in_minutes >= 24 * 60:
        time_in_minutes -= 24 * 60
    hours = str(time_in_minutes // 60)
    minutes = str(time_in_minutes % 60)
    if minutes < "10":
        minutes = "0" + minutes
    time_in_format = hours + ":" + minutes
    # print(time_in_format)
    return time_in_format

# convert_time_in_minutes_to_formatted_time(580)

start_of_shift = start_time_in_minutes
squad_count = 0
for squad in squads:
    number_of_drivers = 0
    l = start_time_in_minutes
    print()
    print("Squad #" + str(squad_count + 1))
    number_of_members_per_squad = len(squad)
    duty_length_per_soldier = time_length * 2 / number_of_members_per_squad
    patrol_length_per_squad = time_length / number_of_squads
    # Having an odd number of soldiers will leave one free of duty, so it should not affect the length per duo:
    patrol_length_per_duo = patrol_length_per_squad / (number_of_members_per_squad // 2)
    if time_length <= 60 * 6:
        print("Drivers will not have any duties")
    elif time_length - patrol_length_per_duo < 60 * 6:
        print("Drivers will not do a full length of patrol; the patrol_length_per_duo must be recalculated")
    else:
        # rearranging the list so that the drivers will be first or last, ensuring continuous sleep
        if squad_count % 2:
            for soldier in squad:
                if soldier.find("(Driver)") == -1:
                    arranged_squad.append(soldier)
            arranged_squads.append(arranged_squad)
            for soldier in squad:
                if soldier.find("(Driver)") != -1:
                    number_of_drivers += 1
                    arranged_squad.append(soldier)
        else:
            for soldier in squad:
                if soldier.find("(Driver)") != -1:
                    number_of_drivers += 1
                    arranged_squad.append(soldier)
            for soldier in squad:
                if soldier.find("(Driver)") == -1:
                    arranged_squad.append(soldier)
            arranged_squads.append(arranged_squad)
        
        print("Patrol shifts:")
        for j in range(len(arranged_squad) // 2):
            j = j * 2
            soldier1 = arranged_squad[j]
            soldier2 = arranged_squad[j + 1]
            patrol_shift_time = convert_time_in_minutes_to_formatted_time(start_of_shift)
            patrol_shift = [patrol_shift_time, soldier1, soldier2]
            print(patrol_shift)
            start_of_shift += int(patrol_length_per_duo)
            patrol_shifts.append(patrol_shift)
        # print(patrol_shifts)

        print("Stove shifts:")
        stove_length_per_soldier = time_length / (number_of_members_per_squad - number_of_drivers)
        # i = start_time_in_minutes
        for k in range(len(arranged_squad)):
            # print(i, l)
            # print(arranged_squad[k])
            if arranged_squad[k].find("(Driver)") == -1:

                stove_shift_time = convert_time_in_minutes_to_formatted_time(l)
                stove_shift = [stove_shift_time, arranged_squad[k]]
                l += int(stove_length_per_soldier)
                # i += int(patrol_length_per_duo)
                print(stove_shift)
            
        arranged_squad = []
        squad_count += 1

# [time, soldier1, soldier2]

# print(arranged_squads)


    




