# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 23:41:24 2022

@author: Thu Beo
"""
# Homework 1: Lam lai cac bai tren lop
# Bai 2: Kiem tra tinh chan le
x = int(input("Nhap vao so nguyen x: "))
print(f"x-{x} la so chan? {x%2 == 0}")
print(f"x-{x} la so le? {x%2 == 1}")

# Bai 3: Kiem tra so
x = int(input("Nhap vao so nguyen x: "))
print(f"x-{x} co nam trong khoang 22-44 khong? {x >= 22 and x <= 44}")
print(f"x-{x} co nam ngoai khoang 22-44 khong? {x <= 22 or x >= 44}")

# Bai 4: Kiem trat ki tu
c = input("Nhap vao 1 ky tu c: ")
print(f"Kiem tra c-{c} co phai la so khong: {c.isnumeric()}")
print(f"Kiem tra c co phai cu cai thuong khong: {c >= a and c <= z}")
print(f"Kiem tra c co phai cu cai thuong khong: {c >= A and c <= Z}")

# Bai 5: Kiem tra nam nhuan
year = int(input("Nhap vao nam ban muon: "))
print(f"Kiem tra nam do co phai nam nhuan: \
      {(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)}")

# Bai 6: Luyen tap 1
N = int(input("Nhap vao so N: "))
if N == 0:
    print(f"{N} = 0")
if N % 2 == 0:
    print(f"{N} la so chan")

# Homework 2: Tim nghiem phuon trinh bac 2
import math
a = float(input("Nhap vao he so a: "))
b = float(input("Nhap vao he so b: "))
c = float(input("Nhap vao he so c: "))
delta = b**2 - 4*a*c
if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh co vo so nghiem!")
        else:
            print("Phuong trinh vo nghiem!")
    else:
        print(f"Phuong trinh co 1 nghiem la {-c/b}")
else:
    if delta < 0:
        print('Phuong trinh vo nghiem!')
    elif delta == 0:
        print(f"Phuong trinh co mot nghiem duy nhat la: {-b/2**a}")
    else:
        print(f"Phuong trinh co hai nghiem. \
              \n Nghiem thu nhat la {(-b + math.sqrt(delta))/(2*a)} \
                 \n Nghiem thu hai la {(-b - math.sqrt(delta))/(2*a)} ")
                 
# Homework 3:
km = float(input("Nhap so km ban da di: "))

if km < 1:
    print("Gia cuoc cua ban la 15000 VND")
elif km < 21:
    print(f"Gia cuoc cua ban la {15000 + (km - 1) * 12000}")
else:
    print(f"Gia cuoc cua ban la {15000 + 20 * 12000 + (km - 1 - 20) * 10000}")
    
# Hackerrank https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true


n = int(input().strip())
if n % 2 == 1:
    print('Weird')
else:
    if n > 2 and n < 5:
        print("Not Weird")
    elif n <= 20:
        print('Weird')
    else:
        print('Not Weird')