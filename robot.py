
last_twenty_data==[]
def collect_data_of_sensor(single_data): #This function takes a single data from sensor and stores it.
    last_twenty_data.append(single_data)

def reduce_up_to_20_data(): #This function provides up to twenty data counts.
    last_twenty_data.pop(0)

def find_average_of_distance(): #This function calculates average of last 20 data.
    total==0
    count==0
    for i in last_twenty_data:
        total+=i
        count+1
    average==total/count
    return average
    
def determine_robot_movement():
    while True:
        collect_data_of_sensor(single_data)

        if len(last_twenty_data)>20:
            reduce_up_to_20_data()
            find_average_of_distance()
            if average >= 10:
                print("Continue.")
            else:
                print("Stop.")
                break


