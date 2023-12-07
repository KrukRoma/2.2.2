#1
a = int(input("Введіть число від 1 до 7 : "))
if a == 1:
    print("Понеділок")
if a == 2:
    print("Вівторок")
if a == 3:
    print("Середа")
if a == 4:
    print("Четвер")
if a == 5:
    print("П'ятниця")
if a == 6:
    print("Субота")
if a == 7:
    print("Неділя")
if a>7:
    print("Такого дня тижня не існує")
if a<1:
    print("Такого дня тижня не існує")

#2
b = int(input("Введіть число від 1 до 12 : "))
if b == 1:
    print("Січень")
if b == 2:
    print("Лютий")
if b == 3:
    print("Березень")
if b == 4:
    print("Квітень")
if b == 5:
    print("Травень")
if b == 6:
    print("Червень")
if b == 7:
    print("Липень")
if b == 8:
    print("Серпень")  
if b == 9:
    print("Вересень")
if b == 10:
    print("Жовтень") 
if b == 11:
    print("Листопад")
if b == 12:
    print("Грудень")
if b>12:
    print("Такого місяця не існує")
if b<1:
    print("Такого місяця не існує")

#3
x = int(input("Enter your number : "))
if x>0:
    print("Number is positive")
if x<0:
    print("Number is negative")
if x==0:
    print("Number is equal to zero")

#4
c = int(input("Введіть перше число : "))
d = int(input("Введіть друге число : "))
if c==d:
    print("Ці числа рівні")
if c>d:
    print(c,d)
if c<d:
    print(d,c)