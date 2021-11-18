#                                  """ DAY_02 """

#grade allotment

marks = int(input("marks obtained: "))

if marks>100:
   print('incorrect')
   
if marks==100 and marks>=90:
   print('A')
   
if marks<90 and marks>=80:
   print('B')

if marks<80 and marks>=70:
   print('C')

if marks<70 and marks>=50:
   print('D')

if marks<50:
   print('fail')
