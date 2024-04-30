a=[10,20,30,40,50,60,70]
print(a[0:4:1])
print(a[2:5:1])
n=a[2:6] # default step value is 1
print(n)
print(a[0:4:2]) #step value is 2
print(a[4:]) # default ending index will be -last one

n=a[3:] # default ending index will be -last one
print(n)
n=a[3::2]
print(n)
n=a[:4] # default starting index will be 0
print(n)