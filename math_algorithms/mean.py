def mean(given_list):
    result = sum(map(int,given_list))/len(given_list)
    #map: str to int (every index of the given_list), round: decimals
    return round(result, 4)