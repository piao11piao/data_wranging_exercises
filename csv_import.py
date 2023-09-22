# import the 'csv' library, which will give us lots of handy code recipes for dealing with our data file

import csv

# open() is a built in function that takes a file name and a 'mode' as parameters. In this example, the file 20200...csv' should be in the same folder as our oython script

source_file = open('202001-citibike-tripdata.csv','r')

# pass our source_file as an ingredient to the csv library's DictReader
citibike_reader = csv.DictReader(source_file)

print(citibike_reader.fieldnames)
