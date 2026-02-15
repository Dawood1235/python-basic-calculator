test = 0
count = 0
res1 = []
res2 = []
while(test!=-1):
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    test = int(input("Enter -1 to stop enttering the number: "))
    res1.append(num1)
    res2.append(num2)

    count+=1


check = int(input("Press 1 for addition, 2 for multiplication, 3 for subtraction, 4 for division"))
for i in range(1,count+1):
    if(check == 1):
        print("Answer for calculation " ,i, res1[i-1]+res2[i-1])
    elif(check == 2):
        print("Answer for calculation " ,i, res1[i-1]*res2[i-1])
    elif(check == 3):
        print("Answer for calculation " ,i, res1[i-1]-res2[i-1])
    elif(check == 4):
        try:
         print("Answer for calculation " ,i, res1[i-1]/res2[i-1])
        except Exception as e:
            print(e)

