import csv

with open("input.csv") as file:
    def find_total_price(num, price_per_one):
        return num * price_per_one
    write_file = open("output.csv", 'w', newline='')
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames
    fieldnames.append('tot')
    writer = csv.DictWriter(write_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        num = float(row['Quantity'])
        price_one = float(row['Price'])
        row['tot'] = find_total_price(num, price_one)
        writer.writerow(row)

    write_file.close()

print("this is input: ")
with open("input.csv") as file:
    file = csv.DictReader(file)
    for row in file:
        print(row)

print("_____________")
print("this is output: ")
with open("output.csv") as file:
    file = csv.DictReader(file)
    for row in file:
        print(row)



with open("output.csv") as file:
    file = csv.DictReader(file)
    tot_value = 0
    for new_row in file:
        tot_value = float(new_row['tot']) + tot_value
print("______________")
print(f"this market worth: {tot_value}")