import cProfile
array=[]
n=int(input("Cantidad de elementos en el array:"))
for i in range(0,n):
   temp=int(input())
   array.append(temp)
# print(array)
for i in range(0,len(array)):
    try:
        mayor
    except NameError:
        mayor = array[i]
    else:
        if array[i] > mayor:
            mayor = array[i]
    try:
        mayor2
    except NameError:
        mayor2 = array[i]
    else:
        if array[i] < mayor:
            mayor2 = array[i]

# print(mayor)
print("El segundo mayor es: " + str(mayor2))
