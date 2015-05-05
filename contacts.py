import csv
from sf_base import get_col_nums, get_cols, get_sfid, clean_file

infile = csv.reader(open('van_contacts.xls'), delimiter='\t')

headers = infile.next()

headers_req = ['My Campaign ID', 'ResultShortName', 'CanvassedBy', 'DateCanvassed', 'ContactTypeName']

col_nums = get_col_nums(headers, headers_req)

outfile = csv.writer(open('sf_upload-contacts.csv', 'w'))

# Headers for uploading new actions in SF
new_headers = ['VANID', 'Result', 'Subject', 'Action_Date', 'Contact Method', 'Name ID', \
	'Additional Comments', 'Record Type ID', 'Priority', 'Status']
added_fields = ['012i0000001Dqri', 'Normal', 'Completed']
outfile.writerow(new_headers)


for row in infile:
	cols = get_cols(row, col_nums)
	if cols[4] not in ('Phone', 'Email', 'Facebook'):
		continue
	else:
		new_row = cols[0:2] + [cols[2]] + cols[3:] + [get_sfid(cols[0])] + [cols[2]] + added_fields
		outfile.writerow(new_row)
