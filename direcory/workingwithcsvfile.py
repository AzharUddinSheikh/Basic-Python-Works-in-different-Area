import csv
'''
with open("data.csv", "w") as file:
    writer = csv.writer(file)
    # so with this we  can simply write tabular data to our csv file
    writer.writerow(['transaction_id', 'price', 'quantity'])
    writer.writerow([1001, 45, 2])
    writer.writerow([1002, 55, 45])
'''

with open('data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) == 0:
            continue
        print(row)
