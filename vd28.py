s = input("nhap xau ky tu: ")

str = list(s)
#xau theo chieu nguoc lai
str.reverse()
str = "".join(str)
print("xau chieu nguoc lai: {}".format(str))