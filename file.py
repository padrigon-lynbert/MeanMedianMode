import os

def cls(): os.system('cls')

class Look:
     def for_mean(data): 
        missing_mean = (sum(data)/len(data))

        return missing_mean
     
     def for_median(data):
        # ( data[len(data)/2] + data[ ( (len(data)/2) +1) ] /2 )

        if (len(data) % 2 == 0): missing_median = (data[int(len(data)/2)] + data[int( (len(data)+1) /2) ]) / 2 #even
        else: missing_median = data[int((len(data)+1)/2)] #odd
          
        return missing_median

     def for_mode(data): pass

def get_input():
        cls()
        data = list()
     
        while True:
            while True:
                input("<ENTER>"); cls()
                print(f"Data: {data}")
                print("<1> Add \n<2> Remove last index \n<3> change nothing and move on")
                try:
                    choice = int(input("\n\n:")); break
                except ValueError: cls(); print("please input a valid number.")
                
            if choice in range(1,4):         
                if choice == 1: 
                    cls() 
                    print("Separate the value using spaces.\n\n"); data = input("Add: ").split()
                elif choice == 2: 
                    try:
                        data.pop()
                    except IndexError: print("Catched no value to delete.")
                else: break

        return data
#uncomment to test mean
"""
data = [1,1,3,4,6,6,8,9]
print(Look.for_mean(data))
"""

#uncomment to test median        
"""
# test 
odd_data = sorted([1,54,56,84,5,2,5])
even_data = sorted([1,1,3,4,6,6,8,9,10,11])

# print(type(even_data))

print(Look.for_median(even_data))
"""