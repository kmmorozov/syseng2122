l1 = ['192.168.20.10',22,'root','123456']
print(l1)
l1.append('dc1')
print(l1)
print(len(l1))
l2 = ['огурцы','помидоры']
l1.extend(l2)
print(l1)
l1.pop(5)
print(l1)
l1.insert(5,'перцы')
print(l1)

print(l1.index('root'))
print(l1.count(22))
#l1.sort()
print(l1)

l1.reverse()
print(l1)

l3 = l1.copy()
l4 = l1
l1.append('!!!!!!!')
 
print('-----------------------------------------------------------------')
print(l3)
print(l4)

a = 10
b = a
a = 123
print(b)
l3.clear()
print(l3)


