# class sinh_vien:
#     def __init__(self, hoten, lop, diemTDC):
#         self.hoten = hoten
#         self.lop = lop
#         self.diemTDC = diemTDC


n = int(input("Nhap so luong sinh vien (5 <= n <= 20): "))
# while n < 5 or n > 20 :
#     print("so luong sv khong hop le")
#     n = int(input("Nhap so luong sinh vien (5 <= n <= 20): "))

print("nhap thong tin sinh vien")
students =[]
for i in range(n):
    name = input("nhap ten:")
    class_name = input("nhap lop: ")
    diem = float(input("diem thi Tin dai cuong: "))

    students.append([name, class_name, diem])

print("danh sach sinh vien vua nhap ")
arr = [print(i,j,k) for i,j,k in students]

x = float(input("nhap so thuc x: "))

print("danh sach sinh vien co diem nho hon {}".format(x))
print('\n'.join([a for a,b,c in students if c < x]))




