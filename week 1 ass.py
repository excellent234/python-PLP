operand = input ('enter + , - , * , / please: ')
num1 , num2 = input('enter first and second number please:').split() 

#note : enetr 
#the first number then space and second number 

num1 =  int(num1)
num2 = int(num2)

if operand == '+':
    print ('your answer is ',num1 + num2)
if operand == '-':
    print ('your answer is ',num1 - num2)
if operand == '/':
    print ('your answer is ',num1 / num2)
if operand == '*':
    print ('your answer is ',num1 * num2)