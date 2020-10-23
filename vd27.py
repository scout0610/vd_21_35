# Chuyen cac ky tu dau moi tu thanh chu hoa, cac ky tu con lai thanh chu thuong
s = input("nhap xau ky tu: ")
str = s.split()

# ky tu dau moi tu thanh chu hoa
a = list(map(lambda i: i[0].upper() , str))

# ky tu con lai thanh chu thuong
b = list(map(lambda i: i[1:].lower() , str))

# ket qua
c = " ".join(list(map(lambda i,j: i+j, a,b)))
print("chuoi moi :{}".format(c))
