
computer_list = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30 
}

computer_list["TOSHIBA"] = 10
computer_update = {"DELL": 60, "MACBOOK": 2}
computer_list.update(computer_update)



# 1
for key, value in computer_list.items():
    print(key, ":", value)

# 2
values_computerList = computer_list.values()
total_computer = sum(values_computerList)
print("Sum of all computers: ", total_computer)

# # 3
computer_list["FUJITSU"] = 5
computer_list["ALIENWARE"] = 15
print(computer_list)


# # 4
values_computerList = computer_list.values()
total_computer = sum(values_computerList)
print("Sum of all computers: ", total_computer)
