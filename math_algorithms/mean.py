def mean(given_list):
    result = sum(map(int,given_list))/len(given_list)
    #map: str to int (every index of the given_list), round: decimals
    return round(result, 4)

# data = [1, 2, 3, 4, 5]

# get_input = input(": ").split()
# data = list(map(int, get_input))

# print(mean(data))