def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
    # sử dụng hàm và in ra kết quả
input_string = input("Mời nhập chuỗi cần đảo ngược:")
print("chuỗi đảo ngược là:", dao_nguoc_chuoi(input_string))