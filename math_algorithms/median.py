def for_median(data):
    # ( data[len(data)/2] + data[ ( (len(data)/2) +1) ] /2 )

    data.sort()

    if (len(data) % 2 == 0): missing_median = (data[int(len(data)/2)] + data[int( (len(data)+1) /2) ]) / 2 #even
    else: missing_median = data[int((len(data)+1)/2)] #odd
        
    return missing_median


data = [3,2,1,5,4]

c = for_median(data)
print(c)
# 