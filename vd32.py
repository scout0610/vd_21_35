# Ham tra ve 1 neu la so nguyen to, tra ve 0 neu khong phai
import math

n = int(input("nhap n: "))


def kiemtra(n):
    flag = 0
    if n==0 or n==1:
        return 1
    for i in range(2, math.ceil(math.sqrt(n)) + 1 ):

        if n% i == 0 and n!= 2 :
            flag = 1
            break
    return flag

if(kiemtra(n)):
    print("n khong la so nguyen to")

else:
    print("n la so nguyen to")


