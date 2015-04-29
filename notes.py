import csv
from sf_base import get_col_nums, get_cols, get_sfid, clean_file

infile = csv.reader(open('van_notes.xls'), delimiter='\t')

headers = infile.next()

headers_req = ['My Campaign ID', 'DateEntered', 'EnteredBy', 'NoteText ']

col_nums = get_col_nums(headers, headers_req)

outfile = csv.writer(open('sf_upload-profile-notes.csv', 'w'))

# Headers for uploading new actions in SF
new_headers = ['VANID', 'Name ID', 'More Notes']
outfile.writerow(new_headers)

notes_by_id = {}
for row in infile:
	cols = get_cols(row, col_nums)
	if not notes_by_id.get(cols[0]):
		notes_by_id[cols[0]] = ' - '.join(cols[1:])
	else:
		notes_by_id[cols[0]] += ('\r\n' + ' - '.join(cols[1:]))

for mycampaign_id, notes in notes_by_id.items():
	outfile.writerow([mycampaign_id, get_sfid(mycampaign_id), notes])