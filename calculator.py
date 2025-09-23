count=int(input('How many numbers do you want?\n'))
i=0
numbers=[]
result = 0
j=0
operand=input("Which operation do you want?\n")
while i<count and count>1:
    number=input("Enter number: ")
    numbers.append(int(number))
    i += 1

print(numbers)

while j<len(numbers):
    if operand=="+":
        result= result+numbers[j]
    elif operand=="-":
        if j==0:
            result=numbers[j]
        else:
            result=result-numbers[j]
    elif operand=='x':
        if j==0:
            result=numbers[j]
        else:
            result=result*numbers[j]
    elif operand=='/':
        for n in numbers:
            if n==0:
                print("cannot divide")
                break
        if j==0:
            result=numbers[j]
        else:
            result= result/numbers[j]


    j += 1

print(result)
    