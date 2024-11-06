

def time_difference(hour1, hour2):
    forward_diff = (hour2 - hour1 + 24) % 24
    backward_diff = (hour1 - hour2 + 24) % 24
    return min(forward_diff, backward_diff)

hour1 = int(input("Hour 1: "))
hour2 = int(input("Hour 2: "))

print("the time difference is: ", time_difference(hour1, hour2))

