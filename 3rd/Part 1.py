# 1
computer_list = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30 
}

# 2
print("MACBOOK has: ", 
    computer_list["MACBOOK"]
)

# 3

key_input = input("Please input a computer brand (HP/DELL/MACBOOK/ASUS): ").upper()
for item in computer_list:
    if key_input == item:
        print(item, computer_list[item])

