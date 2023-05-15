
last_twenty_data = [10]
last_twenty_data.pop()
"""
def collect_data_of_sensor(): #This function takes a single data from sensor and stores it.
    single_data = input("Data from sensor:")
    last_twenty_data.append(single_data)

def collocate_last_20_data(): #This function provides up to twenty data counts.
    
    while True:
        collect_data_of_sensor()
    
        if len(last_twenty_data) > 20:
            last_twenty_data.pop(0)
            print("It's working.", len(last_twenty_data)
            break


"""
def find_average_of_distance(): #This function calculates average of last 20 data.
    total = 0
    count =10 0
    for i in last_twenty_data:
        total+=i
        count+=1
    average = total/count
    return average
    
def determine_robot_movement(): 
    while True:
        collect_data_of_sensor()

        if len(last_twenty_data) > 20:
            collocate_20_data()
            find_average_of_distance()
            if find_average_of_distance() >= 10:
                print ("Continue.")
            else:
                print ("Stop.")
                break

determine_robot_movement()
"""
collocate_last_20_data()