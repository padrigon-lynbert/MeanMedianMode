def mean(given_list):
    result = sum(map(int,given_list))/len(given_list)
    
    return round(result, 4)