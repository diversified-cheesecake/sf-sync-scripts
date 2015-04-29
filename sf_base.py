import csv
from sf_credentials import username, password, security_token

def update_lookuptable():

	from simple_salesforce import Salesforce
	
	outfile = csv.writer(open('sf-van.csv', 'w'))
	outfile.writerow(['sfid', 'vanid'])
	
	sf = Salesforce(username=username, password=password, security_token=security_token)

	query = """
		select Id, VANID__c from Contact 
		where VANID__c != null and RecordType.Name = 'Survivor'
		"""

	results = sf.query_all(query)

	for result in results['records']:
		outfile.writerow([str(result['Id']), str(int(result['VANID__c']))])

update_lookuptable()

def get_col_nums(headers, headers_req):

	''' Get the column numbers specified by a list of columns, based on the file header '''

	col_nums = []
	for header in headers_req:
		try:
			col_nums.append(headers.index(header))
		except:
			continue
	return col_nums

def get_cols(row, col_nums):

	''' Get the columns specified, provided the column numbers wanted '''

	cols = []
	for col_num in col_nums:
		cols.append(row[col_num])
	return cols

def get_sfid(vanid):
	
	''' Submit a VAN My Campaign ID, and then get back the Salesforce ID, if the VAN ID is mapped in Salesforce '''

	infile = csv.reader(open('sf-van.csv'))
	infile.next()
	for row in infile:
		if vanid == row[1]:
			return row[0]
	return None

def clean_file(file_path):
	
	''' take out null bytes '''

	text = open(file_path).read()
	outfile = open(file_path, 'w')
	
	for chr in text:
		if chr != '\x00':
			outfile.write(chr)
		else:
			continue

