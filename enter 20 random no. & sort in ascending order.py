Numbers = []
iterate = 0

while len(Numbers)<20:
    try:
        x = int(input("Insert the 20 random numbers: "))
        Numbers.append(x)
    except:
        print("The input  MUST be a number.")
        continue
    for iteration_count in range(len(Numbers)):
        #This acts like a counting method
        for j in range(0,len(Numbers)-1):
            #It swaps each element for each iteration (j is just a random variable)
            if (Numbers[j]>Numbers[j+1]):
                Numbers[j],Numbers[j+1] = Numbers[j+1],Numbers[j]
print(f"Here are the sorted numbers:{Numbers}")

'''
n = int(input())
random_no = []
for num in range(0,n):
    random = int(input('Enter 10 random no.: '))
    random_no.append(random)
for num in range(len(random_no)):
    for index in range(0,len(random_no)-1):
        if random_no[index] > random_no[index+1]:
            random_no[index],random_no[index+1] = random_no[index+1],random_no[index]
print(random_no)
'''