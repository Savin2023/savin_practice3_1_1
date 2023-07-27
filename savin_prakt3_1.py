# Перемножение векторов
from random import randint

# Функция вывода на печать для наглядности
def print_prod(a,b,n,prod):
    for i in range(n):
        if i!=2:
            print("                    ",b[i])
        else:
            print(a," X  ",b[i])
    print("\nПроизведение:",end=" ")
    for i in range(n):
        if i!=(n-1):
            print(a[i],"x",b[i],"+",end=" ")
        else:
            print(a[i],"x",b[i],end=" ")
    print("=",prod)


# формирование векторов
n=5
vect_a=[]
vect_b=[]
tmp_a=0
tmp_b=0
prod=0


for i in range(n):
    tmp_a=randint(1,9)
    tmp_b=randint(1,9)
    vect_a.append(tmp_a)
    vect_b.append(tmp_b)
    prod+=(tmp_a*tmp_b)
    

print("Вектор а: ",vect_a)
print("Вектор b: ",vect_b)
print()
print_prod(vect_a,vect_b,n,prod)
                  

