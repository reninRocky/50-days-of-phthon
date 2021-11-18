#                                  """ DAY_05 """

#                   Nested if statement
'''
num1=3
num2=4

print("num1 is greater")if(num1>num2) elseprint("num1 and num2 is equal")if(num1==num2) elseprint("num2 is greater") if(num2>num1)

# example of one line execution but error in this correction needed
'''
##a = 50
###a = int(input("enter the no."))
##
##if a <= 100:
##   print("entered no. is greater")
##elif a <= 40:
##     print("entered no. is greater") 
##elif a == 50:
##     print(" a is equal 50")
##else :
##     print("entered no. is not avaliable in thiis table")

#                       check the no.

##num = float(input("enter the no."))
##
##if(num>= 0):
##    if num == 0:
##      print("zero")
##    else:
##      print("positive")
##
##else:
##   print("negative")

#                         Comparison
   
##a=67
##b=57
##if(a>b):
##       pass
##else:
##     print("a is smaller")
##
##li={'a','b','c'}
##
##for i in li:
##    if(i =='a'):
##       pass
##    else:
##        print(i)

#                  switch in if-elif 1 - chocalate, 2- icecream

##def switch():
##    option = int(input("enter your choice: "))
##
##    if option == 1:
##       result = "chocolate"
##       print("you can have", result)
##
##    elif option == 2:
##        result = 'icecream'
##        print("you can have", result)
##
##    else:
##        print("invalid option")

#Switch()

### this switch case can excuted without the switch function but you have to press F5 continuesly for nxt line
##
### nxt method finding switch cas e by using class code -20:22 in day 5 of 50 days of python
##
##
###                       dictionary mapping
##num ={
##'a' : 250,
##'b' = 244,
##'c' : 125,
##}
##inp = input("enter the char")
##print('the result: ',num.get(inp, 7))# 7 will print if the statement is false
##
###                           for loop
##
###                             exp-1
##
## for i in range(4):
##    print('hello')
##
###                             exp-2
##\
##for i in range(2)
##     num =eval(input('enter the value'))
##     print("the square of the value is ', num*num)
##print('the loop is over')
##
###                           write 1 - 10
##
##for i in range(10):#u can put(1,10)
##     print(i+1)
##
##
### range(3,7) - 3,4,5,6
### range (3,9,2) - 3,5,7
##
###                             knowledge
##
##import time
##for i in range(5,0,-1):
##     tim.sleep(3)
##     print(i, end=' ')
##print ('looop is over')
##
###                                 FUN
##
##for i in range(7):
##    print('*'*4)


##for i in range(7):
##    print('*  '*(i+1))

#                             assignment

print(' \nPls give odd no. above 3 for the ootput\n')
n = int(input('Enter the size you want: '))
a = ((n-2)+1)/2
b = n-2
result_str="";    
for row in range(0,n):    
    for column in range(0,n):     
        if (((column == 1 or column == b) and row != 0) or ((row == 0 or row == a) and (column > 1 and column < b))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print('\n'+result_str);

