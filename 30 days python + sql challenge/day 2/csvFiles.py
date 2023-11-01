# working with csv files
print("Working with csv files")

import csv

# reading csv file as list of lists
with open("files/suv_data.csv") as csvfile:
	csvreader = csv.reader(csvfile)
	data = list(csvreader)
	print(data, '\n')

# reading csv file as list of dictionary
with open("files/suv_data.csv", 'r') as csvfile:
	csvreader = csv.DictReader(csvfile)
	data = list(csvreader)
	print(data, '\n')

# writing csv from a list of lists
print("writing csv ffrom a list of lists", '\n')
data = [
     ['Name', 'Age', 'Country'],
     ['Omkar', 20, 'India'],
     ['Chaitanya', 20, 'India'],
     ['Shivam', 20, 'India']
]

with open("files/users.csv", 'w', newline = '') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerows(data)

# writing csv from a list of dictionaries
print("writing csv from a list of dictionaries", '\n')
data = [
    {'Name' : 'Omkar', 'Age' : 20, 'Country' : 'India'},
    {'Name' : 'Shivam', 'Age' : 20, 'Country' : 'India'},
    {'Name' : 'Chaitanya', 'Age' : 20, 'Country' : 'India'}
]

with open("files/users2.csv", 'w', newline = '') as csvfile:
	fieldnames = ['Name', 'Age', 'Country']
	csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
	csvwriter.writeheader()
	csvwriter.writerows(data)

# specifiying delimiters, quotecharcters and handling headers
print("specifiying delimiters, quotecharcters and handling headers", '\n')

with open("files/users.csv", 'r', newline = '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',', quotechar = '`')
	next(csvreader) # skipping attribute names

	next(csvreader) # skipping first row
	data = list(csvreader)
	print(data, '\n')


# Working with csv dialects
print("Working with csv dialects", '\n')

csv.register_dialect('custom', delimiter = ';', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

with open('files/users.csv', 'r', newline = '') as csvfile:
	csvreader = csv.reader(csvfile, dialect = 'custom')

	data = list(csvreader)
	print(data, '\n')