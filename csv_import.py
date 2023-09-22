# import the 'csv' library, which will give us lots of handy code recipes for dealing with our data file

import csv

# open() is a built in function that takes a file name and a 'mode' as parameters. In this example, the file 20200...csv' should be in the same folder as our oython script

source_file = open('202001-citibike-tripdata.csv','r')

# pass our source_file as an ingredient to the csv library's DictReader
citibike_reader = csv.DictReader(source_file)

print(citibike_reader.fieldnames)


# now create our three variables to hold the count of each type
subscriber_count = 0
customer_count = 0
other_user_count = 0

for row in citibike_reader:
	if row['usertype'] == 'Subscriber':
		subscriber_count = subscriber_count + 1
	elif row['usertype'] == 'Customer':
		customer_count = customer_count + 1
	else:
		other_user_count = other_user_count +1
print('Subscribers: ')
print(subscriber_count)
print('customers: ')
print(customer_count)
print('other')
print(other_user_count)
