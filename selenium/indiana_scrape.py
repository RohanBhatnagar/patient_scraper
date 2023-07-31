import csv
from bs4 import BeautifulSoup
import re

def write(data):
	soup = BeautifulSoup(data, 'html.parser')

	shitfix = []
	tables = soup.select(
		'table[border="0"][cellpadding="0"][cellspacing="2"][width="680"]')
	shitfix.append(tables)

	names = []
	addresses = []
	city_state_zips = []
	provider_types = []
	specialties = []
	pd_systems = []
	phones = []
	counties = []


	def parse_string(data):
		for i in range(0, len(data), 1):
			line = data[i]
			if line == "Address:":
				names.append(data[i - 1])
				addresses.append(data[i+1])
			elif line == "City, State, Zip:":
				city_state_zips.append(data[i+1])
			elif line == "Provider Type:":
				provider_types.append(data[i+1])
			elif line == "Specialty:":
				specialties.append(data[i+1])
			elif line == "Program or Delivery System:":
				pd_systems.append(data[i+1])
			elif line == "Phone:":
				phones.append(data[i+1])
			elif line == "County:":
				counties.append(data[i+1])

	def sub_write():
		str = ""
		for table in shitfix:
			spans = soup.select('span', style="font-size:small; font-family:Arial")
			for i in range(0, len(spans), 1):
				str += '\n'
				str += remove_whitespace(spans[i].text)

			arr = str.splitlines()
			parse_string(arr)

			with open('indiana_output.csv', 'w', newline='') as csvfile:
				for i in range(0, len(names), 1):
					csv_line = [names[i], addresses[i], city_state_zips[i], provider_types[i],
								specialties[i], pd_systems[i], phones[i], counties[i]]
					csv_writer = csv.writer(csvfile)
					csv_writer.writerow(csv_line)


	def remove_whitespace(text):
		text = text.strip()
		return re.sub(r'\s{2,}', ' ', text)


	sub_write()
	