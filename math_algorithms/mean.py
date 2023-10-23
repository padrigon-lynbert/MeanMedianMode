def mean(given_list):
    result = sum(map(float,given_list))/len(given_list)
    #map: str to float (every index of the given_list), round: decimals
    return round(result, 4)