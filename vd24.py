n = int(input("nhap so phan tu: "))
arr= [int(input()) for _ in range(n)]
arr.sort()
#Nhap so x va chen vao dung vi tri
x = int(input("nhap x: "))

for i in arr:
    if arr[i] > x:
        break

arr.insert(i, x)
print(arr)