import statistics

data = [1,1,3,4,6,6,8,9]

def mode(lst):
    mode = statistics.mode(lst)
    
    return mode

print(mode(data))
    