def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element
input_tuple = eval(input("Nhập một tuple (phân tách bằng dấu phẩy): "))
first, last = truy_cap_phan_tu(input_tuple)
print("Phần tử đầu tiên của tuple: ", first)
print("Phần tử cuối cùng của tuple: ", last)