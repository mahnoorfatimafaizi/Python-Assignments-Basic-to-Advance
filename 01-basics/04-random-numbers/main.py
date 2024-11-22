import random 

MIN_NUMBER: int = 1
MAX_NUMBER: int = 100
NUMBER_RANGE: int = 10  

number_list = []
for i in range(NUMBER_RANGE):
    rand_number = random.randint(MIN_NUMBER,MAX_NUMBER)
    number_list.append(rand_number)
    print(rand_number, end=" ")
