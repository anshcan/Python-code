list = [1,2,3,4,5,6,7,8,9,10]
print (list)
add=0
for i in range(0,10):
    print("Index-",i," value-",list[i])
    add+=list[i]
print (add)

print("Sum:",sum(list))
print("Max:",max(list))
print("Min:",min(list))
print("Len:",len(list))