#задание 3,4
import json
import csv

data = {
    123456: ('Karl', 25),
    234567: ('Zoi', 30),
    345678: ('Kate', 40),
    456789: ('Mari', 20),
    567890: ('John', 35),
}

with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json", "r") as file:
    data = json.load(file)

field_names = ['ID', 'Имя', 'Возраст', 'телефон']

with open("data.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)

    writer.writeheader()

    for id, values in data.items():
        writer.writerow({'ID': id, 'Имя': values[0], 'Возраст': values[1], 'телефон': ''})