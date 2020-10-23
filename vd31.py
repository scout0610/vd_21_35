PI = 3.14

def chuvi(r):
     return 2*r*PI

def dientich(r):
    return r*r*PI

r = float(input("nhap ban kinh: "))
print("chi vi hinh tron: {}".format('%.2f'%(chuvi(r))))
print("dien tich hinh tron: {}".format('%.2f'%(dientich(r))))

