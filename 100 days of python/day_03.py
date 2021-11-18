#                                  """ DAY_03 """

"""#python as calculator

toffe = 50
qty = 20
tax = 0.18

amount = toffe * (qty + tax)

print(amount)

print("*")
print("* *")
print("* * *")
print("* * * *")
print("* * * * *")"""

###introduction
##name = input("YOUR NAME: ")
##age = int(input("YOUR AGE: "))
##gender = input("ARE YOU (MALE/FEAMLE): ")
##place = input("YOUR ADDRESS: ")
##
###output in arranged order
##design = "||--------<>*****<>---------||"
## print("/n", design)
## print("/t", name)
## print("/t", age)
## print("/t", gender)
## print("/t", place)
## print(design)

 
# wap that prompts user to calculate SI

P = int(input("enter the principle: "))
T = int(input("enter the time: "))
R = int(input("enter the rate: "))
I = int(input("enter the interest: "))

SI = (P*T*R)/100
amount = P+I

print("SI=",SI,"/t","amount=",amount)

