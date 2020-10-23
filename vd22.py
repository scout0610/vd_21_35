n = int(input("nhap so phan tu: "))
arr = [int(input()) for _ in range(n)]

# list so chan
even_arr = [i for i in arr if i % 2 ==0]

#list so le
odd_arr = [i for i in arr if i % 2 !=0]

#Chuyen cac so le len dau day, so chan ve cuoi day
new_arr = odd_arr + even_arr
print(new_arr)
