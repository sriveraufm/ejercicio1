import cProfile
array=[0, 1,3,5,4, -1,6,7]
mayor = array[0]
mayor2 = array[0]
for i in range(0,len(array)):
   if array[i] >= mayor:
       mayor = array[i]
# print(mayor)

for i in range(0,len(array)):
       if array[i] > mayor2:
           for j in range(0,len(array)):
               if array[i] > array[j] and array[i] != mayor:
                   mayor2 = array[i]
print("Del siguiente array: ")
print(array)
print("El segundo mayor es: " + str(mayor2))
# array2 = [len(array)]
# for i in range(0,len(array)):
#     if(array[i])

    

# # print(mayor)
# print("El segundo mayor es: " + str(mayor2))
