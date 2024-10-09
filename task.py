import json
def task_1():
    document = open("task_1.txt", "r")
    total = 0
    for number in document:
        total += int(number)
    document.close
    return total

def task_2():
    total = 0
    loop = "Yes"
    menu = input("Please enter your item codes: ")
    menu = menu.split(",")
    menu = list(menu)
    for item in menu:
        document = open("menu.csv", "r")
        for line in document:
            line = line.split(",")
            if item == line[0]:
                cost = line[2]
                cost = cost.strip()
                total += float(cost)
    document.close
    return round(total, 2)

def task_3():
    check_name = input("Please enter a name: ")
    document = open("contacts.json", "r")
    contacts = json.load(document)
    for key, line in contacts.items():
        value = contacts[key]
        #value = line.values()
        text = key
        new_set = []
        if text == check_name:
            for key2 in value:
                new_set.append(value[key2])
            document.close()
            return (f"Number: {new_set[0]}, Email: {new_set[1]}")
        #print(text)
    document.close()
    return "User not found."
