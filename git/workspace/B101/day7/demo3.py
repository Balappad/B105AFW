# list1=[10,20,30]
# print(list1)
# list2=[10,20,30]
# print(list2)
#
# list1[0]=100
# print(list1)#100,20,30
#
# print(list2) #10,20,30
# #-----------------
# i=10
# print(i)
# j=i #create variable j and copy value from i  and paste it
# print(j)
#
# j=20
# print(i)
# print(j)
#
list1=[10,20,30]
print(list1)

list2=list1 # create list2 and it will point to the same list which is ref by list1
print(list2)

list2[0]=100
print(list1) #100,20,30
print(list2)  #100,20,30

