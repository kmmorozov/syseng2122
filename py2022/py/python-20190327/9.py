arr2=[5,4,3,2,1,3,4,6,5,4]



#
#print(arr2)
#
print(arr2.index(3,3,6))
print(arr2.count(5))
arr2.sort()
print(arr2)
arr2.reverse()
print(arr2)
arr2.remove(4)
print(arr2)
print('-------------------')
print(arr2.count(4))


arr3=arr2.copy()
print(arr3)
arr2[2]=111111111
print(arr2)
print(arr3)


arr2=[5,4,3,2,1,3,4,6,5,4]
arr4=[5,4,345,22,1,55,4,44,5,4]
arr5=[8,4,0,2,1,3,4,2,-8,4]
#
#
arr3 = [arr2,arr4,arr5]
#
print(arr3[1][2])

arr2.append(10)
print(arr2)
arr2.remove(4)
print(arr2)
print(arr2.pop(0))
print(arr2)
arr2.reverse()
print(arr2)
arr2.sort()
print(arr2)
for i in range(0,len(arr2)):
    a=arr2.pop()
    print(a)
    print(arr2)
##
#
print(len(arr2))
