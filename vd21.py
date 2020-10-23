n = int(input("nhap so phan tu: "))
arr = [int(input()) for _ in range(n)]
ori_arr = arr.copy()
arr.sort()

# kiem tra
if arr == ori_arr:
    print("day tang dan")

else:
    arr.reverse()
    if arr == ori_arr:
        print("day giam dan")
    else:
        print("day khong tang dan va khong giam dan")

