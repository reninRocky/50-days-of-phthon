#                                  """ DAY_08 """

##thu- 19/11/21

#Join (opposite of split)
#string join

##li = ['r','e','n','i','n']
##print(' '.join(li))

# list creation with modification

##li = [i+1 for i in range(5)]
##print(li)
##
##nl = [i*2 for i in li]
##print(nl)
##
##nw = [i for i in nl if(i<5)]
##print(nw)

#list with length counting

##alp = ['one','two','three','four','five']
##
##for i in alp:
##    if len(alp) == 3:
##        print(alp[0])
##      #need correction and understanding

### 2d print
##
##data = [['hi','one',1]
##        ['bye','two',2]]
##
##print(data[1][1])
##
### word shuffler word gernator

##from random import shuffle
##word = input('Enter the word: ')
##
##letter_list = list(word)
##shuffle(letter_list)
##
##word = ' '.join(letter_list)
##print(word)

## 2D list

##li = [[1,2,3,4],
##     [5,6,7,8],
##     [9,10,11,12]]
##
##for r in range(3):
##    for c in range(4):
##        print(li[r][c], end=' ')
##    print()
##
###another way
##from pprint import pprint
##pprint(li)

# assignment

# simplified version of yest assign by list method

num_r = 0

ques = ['what is the capital of india: ','what is capital of karnataka: ']
answ = ['New Delhi','Banglore']

for i in range(len(ques)):
    guess = input(ques[i])
    if guess==answ[i]:
        print('correct')
        num_r=num_r + 1
    else:
        print('incorrect\n the answer is ',answ[i])

print('you have',num_r,'out of', i+1, 'right')
