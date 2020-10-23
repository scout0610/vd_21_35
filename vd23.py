n = int(input("nhap so phan tu: "))
a = [int(input()) for _ in range(n)]
#Sap xep cac so le tang dan, so chan giam dan
for i in range(0,n-1):
    for j in range(i+1, n):
        if (a[i] % 2 == 0 and a[j] % 2 == 0 and a[i] < a[j]) or	(a[i] % 2 == 1 and a[j] % 2 == 1 and a[i] > a[j]):
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp

print("mang sau khi sap xep: ")
print(a)

