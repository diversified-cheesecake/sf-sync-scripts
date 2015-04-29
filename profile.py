import csv
from sf_base import get_col_nums, get_cols, get_sfid, clean_file

clean_file('van_profile.xls')

infile = csv.reader(open('van_profile.xls'), delimiter='\t')

headers = infile.next()

headers_req = ['My Campaign ID', 'LastName', 'FirstName', 'MiddleName', \
	'mAddress', 'mCity', 'mState', 'mZip5', 'HomePhone', 'CellPhone', \
	'MSQ:Coalition_Status', 'CreatedBy', 'Notes ']

col_nums = get_col_nums(headers, headers_req)

file_new = csv.writer(open('sf_upload-new-profiles.csv', 'w'))
file_update = csv.writer(open('sf_upload-profile-updates.csv', 'w'))

# Headers for uploading new records into SF
new_headers_new = ['VANID', 'LastName', 'FirstName', \
	'MailingStreet', 'MailingCity', 'MailingState', 'MailingPostalCode', 'Phone', 'MobilePhone', \
	'Survivor Status', 'Coalition Point of Contact', 'More Notes', \
	'Record Type ID', 'Office Name']
added_fields = ['012i0000000NkCg', '001i000000Mu9S7']
file_new.writerow(new_headers_new)

#Headers for updating records in SF
new_headers_update = ['id', 'LastName', 'FirstName', \
	'MailingStreet', 'MailingCity', 'MailingState', 'MailingPostalCode', 'Phone', 'MobilePhone', \
	'Coalition Status', 'Coalition Point of Contact', 'More Notes']
file_update.writerow(new_headers_update)


for row in infile:
	cols = get_cols(row, col_nums)
	if not get_sfid(cols[0]):
		new_row = cols[0:2] + [' '.join(cols[2:4])] + cols[4:12] + [cols[12]] + added_fields
		file_new.writerow(new_row)
	else:
		new_row = [get_sfid(cols[0])] + [cols[1]] + [' '.join(cols[2:4])] + cols[4:12] + [cols[12]]
		file_update.writerow(new_row)