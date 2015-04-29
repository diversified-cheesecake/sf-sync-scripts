import csv
from sf_base import get_col_nums, get_cols, get_sfid

# def get_col_nums(headers, headers_req):
# 	col_nums = []
# 	for header in headers_req:
# 		try:
# 			col_nums.append(headers.index(header))
# 		except:
# 			continue
# 	return col_nums
# 
# def get_cols(row, col_nums):
# 	cols = []
# 	for col_num in col_nums:
# 		cols.append(row[col_num])
# 	return cols
# 
# def get_sfid(vanid):
# 	infile = csv.reader(open('sf-van.csv'))
# 	infile.next()
# 	for row in infile:
# 		if vanid == row[1]:
# 			return row[0]
# 	return None

def get_action(van_role):
	if van_role == 'Host':
		return 'Event: To Host'
	return 'Event: To Attend'


infile = csv.reader(open('van_event_export.xls'), delimiter='\t')

headers = infile.next()

headers_req = ['MyCampaignID', 'EventType', 'EventName', 'Role', 'StartDate', 'STATE', 'Status', 'RecruitedBy']

col_nums = get_col_nums(headers, headers_req)

outfile = csv.writer(open('sf_upload-events.csv', 'w'))

# Headers for Salesforce, and define preset data fields
new_headers = ['VANID', 'Subject', 'Which Action?', 'Action_Date', 'Event_State', 'Result', 'Additional Comments', 'Name ID', \
	'Record Type ID', 'Action Taker Type', 'Priority', 'Status']
added_fields = ['012i0000001DsbH', 'Survivor', 'Normal', 'Completed']
outfile.writerow(new_headers)

for row in infile:
	cols = get_cols(row, col_nums)
	if get_sfid(cols[0]):
		new_row = [cols[0]] + [': '.join(cols[1:3])] + [get_action(cols[3])] + cols[4:] + [get_sfid(cols[0])] + added_fields
		outfile.writerow(new_row)
