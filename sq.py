import csv
from sf_base import get_col_nums, get_cols, get_sfid, clean_file

infile = csv.reader(open('van_sq.xls'), delimiter='\t')

headers = infile.next()

headers_req = ['My Campaign ID', 'CanvassedBy', 'DateCanvassed']

col_nums = get_col_nums(headers, headers_req)

file_new = csv.writer(open('sf_upload-point_of_contact.csv', 'w'))

# Headers for uploading new records into SF
new_headers_new = ['VANID', 'Coalition Point of Contact', 'Coalition Join Date', 'Contact ID']
file_new.writerow(new_headers_new)


for row in infile:
	cols = get_cols(row, col_nums)
	new_row = cols + [get_sfid(cols[0])]
	file_new.writerow(new_row)