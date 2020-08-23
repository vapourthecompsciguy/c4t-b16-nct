

personInfo = {
    "name": "Hiep",
    "class": "AS-Levels",
    "age": 12,
    "school": ["Vinschool", "SIS", "Hanoi Academy"]
}

print(personInfo["class"]) # Get value from Key of Dictionary

personInfo['age'] = 17

print(personInfo)


classSummaries = [
    {
        "name": "A",
        "grade": 8.0,
        "age": 17,
        "class": "C4T-B16",
        "fav": ["Valorant", "CS:GO", "League of Legends"]
    },
    {
        "name": "B",
        "grade": 9.0,
        "age": 17,
        "class": "C4T-B16",
        "fav": ["Gambling", "Reading", "Basketball"]
    },
    {
        "name": "C",
        "grade": 9.5,
        "age": 17,
        "class": "C4T-B16",
        "fav": ["Studying", "hacking", "Soccer"]
    }
]

print(len(classSummaries))

newStudent = {
      "name": "D",
        "grade": 8.5,
        "age": 17,
        "class": "C4T-B16",
        "fav": ["Badminton", "Cycling", "Blackjack"]
    }

classSummaries.append(newStudent)

classSummaries[0]["grade"] = 8.5
print(classSummaries[0]) #the [item] is to display the index of that item

print(len(classSummaries))

newStudent2 = {
    "name": input("Enter your name:"),
    "grade": input("Enter your grade:"),
    "age": input("Enter your age:"),
    "class": input("Enter your class:"),
    "fav": ["Badminton", "Cycling", "Blackjack"]
}

print(newStudent2)

classSummaries.append(newStudent2)

print(classSummaries)

# inputing item into a list

fav = []
n = int(input("How many things do you like to do?:"))

for i in range (0,n):
    element = input("What do you like to do?")
    fav.append(element)

newStudent3 = {
    "name": input("Enter your name:"),
    "grade": input("Enter your grade:"),
    "age": input("Enter your age:"),
    "class": input("Enter your class:"),
    "fav": fav
}

print(newStudent3)







