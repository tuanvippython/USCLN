def UCLN(x,y):
    # Kiểm tra nếu x bằng 0 thì sẽ trả về giá trị y
    if x == 0:
        return y
    else:
    # Nếu x khác 0 thì sẽ lấy phần dư của y chia cho x rồi gán phần dư đó cho giá trị r
    # Sau đó gán giá trị x bằng r và y bằng x, thực hiện phép tính cho đến khi phần dư bằng 0 thì in kết quả ra màn hình
        r = y % x
        return UCLN(r,x)

x = int(input("Nhập giá trị x: "))
y = int(input("Nhập giá trị y: "))

print("ước chung lớn nhất của x và y là: ",UCLN(x,y))

# ví dụ dễ hiểu:
# 12 và 17 (thực hiện chia lấy phần dư y % x sau đó gán cho r, x = 12 | y = 17)
# 17 chia 12 phần dư là 5 (thực hiện chia lấy phần dư x % r , r = 5 | x = 12) 
# 12 chia 5 phần dư 2 
# 5 chia 2 phần dư là 1
# vì 2 chia 1 phần dư là 0 nên ta lấy phần dư trước đó là ước chung của 17 và 12 là 1