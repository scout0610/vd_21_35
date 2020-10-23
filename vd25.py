# Nhap xau ky tu
# Dem so ky tu chu hoa, chu thuong va chu so

s = input("nhap xau ky tu: ")
a = 0
b = 0
c = 0
for i in range(0, len(s)):
    if s[i].isupper(): a+=1
    if s[i].islower(): b+=1
    if s[i].isdigit(): c+=1

print("so ky tu chu hoa: {}".format(a))
print("so ky tu chu thuong: {}".format(b))
print("so ky tu chu so: {}".format(c))

