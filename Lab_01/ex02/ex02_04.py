# tạo một danh sách rỗng lưu kết quả
j=[]
#duyệt qua tất cả các số trong đoạn từ 2000 đén 3200, kiểm tra xem số i có chia hết cho 7 và không phải là bội số của 5 không
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 !=0):
        j.append(str(i))
print(','.join(j))
