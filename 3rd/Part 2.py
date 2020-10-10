# 1

computer_list = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30 
}

computer_list["TOSHIBA"] = 10
print(computer_list)

# 2
new_computer_key = str(input("Pleae input a new computer brand in the dictionary: ")).upper()
new_computer_value = int(input("Please input number of computer of this brand: "))

computer_list[new_computer_key] = new_computer_value
print(computer_list)

# 3
computer_update = {"DELL": 60, "MACBOOK": 2}
computer_list.update(computer_update)
print(computer_list)


