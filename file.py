import os

def cls(): os.system('cls')

class Look:
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
        
Look.get_input()