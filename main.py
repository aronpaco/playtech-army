with open('document.txt', 'r') as file:
    timeframe = file.readline().strip()

print(timeframe)
    
    
# def calculate_timeframe(timeframe):
start_time, end_time = timeframe.split(" - ")

print(start_time)
print(end_time)



