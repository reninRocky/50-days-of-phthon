###                                  """ DAY_09 & 10 """
##
####sun- 21/11/21
##
###TUPLES ()
##
####subj = ("math","eng","sci") #allow duplicate
####num_boolean = tuple((1,2,True,False))
####print(subj[0])#single tuple with one variable without comma not defined
####print(len(subj))
####print(num_boolean)
####print(type(subj))
##
###change tuple value
##
###soln #1) convert to list
##      #2) add the new item
##      #3) finally conevert back to tuple
##
##subj = ("math","eng","sci")
##print(subj)
##
##subj1 = list(subj)
##subj1.remove('math')
##subj1[0] = "phy"
##print(subj1)
##
##subj = tuple(subj1)
##print(subj)
##
### can we add tuple
##
##obj = ("table","cable")
##obj1 = ("bed","soya")
###add obj + obj1
##obj+=obj1
##print(obj)
##
###tuple unpacking
##
##subj = ("math","eng","sci")
###unpacking
##(ii,ie,ir) = subj
##print(ii)
##print(ie)
##print(ir)
##
###loop in tuple
##
##subj = ("math","sci","eng")
##for cls in subj:
##    print(cls)
##
##################################
##    #intro of sets
###creating of set?----{}
##
##subj = {"math","sci","eng"}
##print(subj)
##print(len(subj))
##print(type(subj))
##
##subj = set(("math","eng","sci"))
##print(subj)
