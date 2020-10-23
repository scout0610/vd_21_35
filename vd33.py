n = int(input("nhap so phan tu: "))
print("nhap mang")
arr = [int(input()) for _ in range(n)]

print("xuat mang")
x = [print(i) for i in arr]

arr.sort()
print("sap xep {}".format(arr))

print("so lon nhat {}".format(arr[n-1]))