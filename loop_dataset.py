# create a list that contains the number of pages in each chapter
# of the print version of this book

page_counts = [28, 32, 44, 23, 56, 32, 12, 34, 30]

# create a variable to keep track of the total number of pages,
# starting ins value at 0

total_pages = 0


# use built-in sum function
print(sum(page_counts))

for a_number in page_counts:
	print('TOP of loop!')
	print('the current item is:')
	print(a_number)
	total_pages = total_pages + a_number
	print('bottom of loop')
print(total_pages)

def count_pages(page_count_list):
	total_pages = 0
	under_30 = 0
	over_30 =0
	for a_page in page_count_list:
		total_pages = total_pages + a_page
		if a_page > 30:
			over_30 = over_30 + 1

		else:
			under_30 = under_30 + 1
	print(total_pages)
	print(over_30)
	print(under_30)


count_pages(page_counts)

