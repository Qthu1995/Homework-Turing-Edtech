#1. Yêu cầu nhập vào tên người dùng, xuất ra dòng “Xin chào ” + tên người dùng. 
userName = input("Nhap vao ten nguoi dung: ")
print(f"Hello {userName}")

#2. Viết chương trình tính trung bình cộng của 3 số thực.
a1 = float(input("Nhap so thu 1: "))
a2 = float(input("Nhap so thu 2: "))
a3 = float(input("Nhap so thu 3: "))
print(f"Trung binh cong cua 3 so la: {(a1+a2+a3)/3}")

#3. Yêu cầu nhập chiều cao (h), cân nặng (w). Tính chỉ số BMI (Cân nặng / chiều cao2). 
h = float(input("Nhap chieu ca h (m): "))
w = float(input("Nhap can nang w (kg): "))
print(f"Chi so IBM cua ban la: {round(w/(h**2), 2)}")

# 4. Viết chương trình nhập 3 số nguyên a, b, c (a != 0); tìm nghiệm của phương trình ax+b=c 
a = int(input("Nhap so nguyen a khac 0: "))
b = int(input("Nhap so nguyen b: "))
c = int(input("Nhap so nguyen c: "))
print(f"Nghiem cua phuong trinh ax + b = c la x = {(c - b)/a}")

#5. Viết chương trình nhập bán kính của 1 đường tròn; tính chu vi & diện tích của đường tròn đó 
import math
R = float(input("Nhap ban kinh duong tron: "))
print(f"Chu vi cua duong tron la: {round(2*math.pi*R, 2)}")
print(f"Ban kinh cua duong tron la: {round(R**2*math.pi, 2)}")

# 6. Viết chương trình nhập số nguyên dương n; tính tổng của 1 đến n. 
n = int(input("Nhap so nguyen duong n: "))
print(f"Tong cua chuoi tu 1 den n la: {int(n*(n+1)/2)}")