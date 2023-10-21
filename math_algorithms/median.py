def median(given_list):

    given_list.sort()

    if (len(given_list)%2 == 0): median = ((len(given_list)/2) + ((len(given_list)/2)+1)) / 2 #even
    else: median = (len(given_list) + 1) / 2 #odd
    
    return median