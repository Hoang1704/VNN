import os
#in ra tất cả các tệp/thư mục của đường dẫn được truyền vào
a = os.listdir("/home/hoang/Desktop/qa")
for i in range(0,len(a)):
    if a[i] == 'vn':
        print(a[i])