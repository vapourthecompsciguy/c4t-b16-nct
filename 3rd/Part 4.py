# 1
computer_list_cost = {
    "HP": 600 ,
    "DELL": 650,
    "MACBOOK": 12000,
    "ASUS": 400,
    "ACER": 350,
    "TOSHIBA": 600,
    "FUJITSU": 900,
    "ALIENWARE": 1000 
}

print(computer_list_cost)

# 2
print("ASUS has: ", 
    computer_list_cost["ASUS"]
)


# 3
key_input = input("Please input a computer brand (HP/DELL/MACBOOK/ASUS/ACER/TOSHI/FUJITSU/ALIENWARE): ").upper()
for item in computer_list_cost:
    if key_input == item:
        print(item, computer_list_cost[item])