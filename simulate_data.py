import json
import random
import copy

VATNO = 1234567
PRODUCTID = 6231245
PRODUCTEAN = 8231246

def next_ProductID():
	global PRODUCTID
	PRODUCTID = PRODUCTID + 1
	return PRODUCTID

def next_ProductEAN():
	global PRODUCTEAN
	PRODUCTEAN = PRODUCTEAN + 1
	return PRODUCTEAN

key_naming = ["one", "two", "three", "four", "five", "six", "seven"]
Malaria = { 'one': {'coartem':[next_ProductEAN(), next_ProductID()],
			'parecetamol':[next_ProductEAN(), next_ProductID()]},

			'two': {'coartem':[next_ProductEAN(), next_ProductID()],
			'oxymetazoline':[next_ProductEAN(), next_ProductID()]},

			'three': {'artemether':[next_ProductEAN(), next_ProductID()],
			'antacid':[next_ProductEAN(), next_ProductID()]}
		  }

TB = {
		'one': {'rifater':[next_ProductEAN(), next_ProductID()],
			'phenylphrine':[next_ProductEAN(), next_ProductID()]},

		'two': {'aifampicin':[next_ProductEAN(), next_ProductID()],
			'cetrizine':[next_ProductEAN(), next_ProductID()]},

		'three': {'myambutol':[next_ProductEAN(), next_ProductID()],
			'flagyl':[next_ProductEAN(), next_ProductID()]},

		'four': {'rifamate':[next_ProductEAN(), next_ProductID()],
			'tylenol':[next_ProductEAN(), next_ProductID()]}
	}

Jaundice = {
			'one': {'Repamerz':[next_ProductEAN(), next_ProductID()],
					'zantac':[next_ProductEAN(), next_ProductID()]},

			'two': {'silibinin':[next_ProductEAN(), next_ProductID()],
					'metronidazole':[next_ProductEAN(), next_ProductID()]},

			'three': {'silibinin':[next_ProductEAN(), next_ProductID()],
					  'paracetamol':[next_ProductEAN(), next_ProductID()]},

			'four': {'denamarin':[next_ProductEAN(), next_ProductID()],
					 'nimesulide':[next_ProductEAN(), next_ProductID()]}
		  }

Diarrhoea = {
			 'one': {'metronidazole':[next_ProductEAN(), next_ProductID()],
			'paracetamol':[next_ProductEAN(), next_ProductID()]},

			'two': {'tinidazole':[next_ProductEAN(), next_ProductID()],
			'antacid':[next_ProductEAN(), next_ProductID()]},

			'three': {'loperamide':[next_ProductEAN(), next_ProductID()]}
		  }

Diseases = [Malaria, TB, Jaundice, Diarrhoea]

Random = {
			'Aluminium Forearm Crutches Adult':[next_ProductEAN(), next_ProductID()],
			'Blade':[next_ProductEAN(), next_ProductID()],
			'Bandage':[next_ProductEAN(), next_ProductID()],
			'Coke':[next_ProductEAN(), next_ProductID()],
			'Dettol':[next_ProductEAN(), next_ProductID()],
			'Creme':[next_ProductEAN(), next_ProductID()],
			'Balm':[next_ProductEAN(), next_ProductID()]
		 }

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
	dummy_product = data['products'][0]
	zipcodes = get_zipcodes(zipcode_file)

	for i in range(count):
		path = "./data/"
		filename = path + str(i) + "simulated_data.json"
		with open(filename, "w+") as fout:
			new_zipcode = zipcodes[random.randint(0, len(zipcodes) - 1)]
			new_VATNumber = 'FI' + str(next_VATNumber()) 
			data["sellerInformation"]["sellerAddress"]["zipCode"] = str(new_zipcode)
			data["sellerInformation"]["sellerVATNumber"] = new_VATNumber
			data["receiptTimestamp"] = data["receiptTimestamp"] + 10

			disease = Diseases[random.randint(0, len(Diseases) - 1)]
			value = disease[key_naming[random.randint(0, len(disease.items()) - 1)]]

			something = []
			print(value)
			for key in value.keys():
				print(key)
				dummy_product['productName'] = key
				dummy_product['productEANCode'] = value[key][0]
				dummy_product['productId'] = value[key][1]
				abc = copy.deepcopy(dummy_product)
				something.append(abc)

			data['products'] = something
			print(something)
			print("-" * 40)
			print(data)
			fout.writelines(json.dumps(data, indent=4, sort_keys=True))

if __name__ == '__main__':
	simulate_data("helsinki_zipcodes.txt", 1000)
