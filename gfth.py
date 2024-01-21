#2
for i in range(1, 11):
    for j in range(1, 11):
        print ('{} x {} = {}'.format(i, j, i*j), end=' ')
    print()
#3

numb = int(input(" Enter a number : "))

# using the for loop to generate the multiplication tables

print("Table of: ")

for a in range(1,11):

   print(numb,'x',a,'=',numb*a)
   #1
diapazonn = int(input("Введите начало диапазона для поиска простых чисел: "))
diapazonk = int(input("Введите конец диапазона для поиска простых чисел: "))
for num in range(diapazonn, diapazonk):
    count = 0
    delitel = 2
    while delitel < num:
        if num % delitel == 0:
            count += 1
        delitel += 1
    if count == 0:
        print(f'{num} простое число')



