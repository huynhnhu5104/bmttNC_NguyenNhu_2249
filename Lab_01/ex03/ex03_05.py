def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

#nhập ds từ ng dùng
input_string = input("nhập ds các từ, cách nhau bằng dấu cách:")
word_list = input_string.split()

#sd hàm và in ra kq
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("số lần xuất hiện của các phần tử:", so_lan_xuat_hien)