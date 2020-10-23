import math

def khoangcach (p1, p2):
    return math.sqrt(math.pow(int(p1[0]) - int(p2[0]), 2) + math.pow(int(p1[1]) - int(p2[1]), 2) + math.pow(int(p1[2]) - int(p2[2]), 2))


p1 = input("nhap toa do diem 1: ").split()
p2 = input("nhap toa do diem 2: ").split()

print("khoang cach 2 diem : {}".format(khoangcach(p1,p2)))

def trungdiem(x,y):
    return (x+y) /2

print("toa do trung diem {} {} {}".format(trungdiem(int(p1[0]), int(p2[0])),trungdiem(int(p1[1]), int(p2[1])), trungdiem(int(p1[2]), int(p2[2])) ))


