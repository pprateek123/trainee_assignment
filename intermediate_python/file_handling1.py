import csv

with open('data.csv', 'r') as input_csv_file:
    csv_reader = csv.DictReader(input_csv_file)
    
    adults = []
    
    for row in csv_reader:
        if int(row['Age']) >= 18:
            adults.append(row)

with open('adults.csv', 'w', newline='') as output_csv_file:
    fieldnames = ['Name', 'Age']
    csv_writer = csv.DictWriter(output_csv_file, fieldnames=fieldnames)
    
    csv_writer.writeheader()
    
    csv_writer.writerows(adults)






