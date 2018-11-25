import json
import random

VATNO = 1234567

def next_VATNumber():
	global VATNO
	VATNO = VATNO + 1
	return VATNO

def get_zipcodes(filename):
	with open(filename, 'r') as fin:
		lines = fin.readlines()

	lines = [lines[i].strip() for i in range(len(lines))]

	return lines
	
def get_sample_req():
	filename = "receipthero_get.json"
	with open(filename, 'r') as fin:
		lines = fin.readlines()

	line = "".join(lines)
	data = json.loads(line)

	return data

def simulate_data(zipcode_file, count):
	data = get_sample_req()
	zipcodes = get_zipcodes(zipcode_file)

	for i in range(count):
		path = "./data/"
		filename = path + str(i) + "simulated_data.json"
		with open(filename, "w+") as fout:
			new_zipcode = zipcodes[random.randint(0, len(zipcodes) - 1)]
			new_VATNumber = 'FI' + str(next_VATNumber()) 
			data["sellerInformation"]["sellerAddress"]["zipCode"] = str(new_zipcode)
			data["sellerInformation"]["sellerVATNumber"] = new_VATNumber
			fout.writelines(json.dumps(data, indent=4, sort_keys=True))

