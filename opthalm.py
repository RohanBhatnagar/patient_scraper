import requests
import sys
from bs4 import BeautifulSoup
import numpy as np
import json
import math
import pandas as pd
import csv
# import csv

# csv_file = "data.csv"

# test = {
#     "field 1": "hio",
#     "field 2": "hi2"
# }

# field_names = ["field 1", "field 2"]
# # Open the CSV file in append mode and write the new row
# with open(csv_file, 'a', newline='') as f:
#     writer = csv.DictWriter(f, field_names)

#     # Write the new row (dictionary) to the CSV file
#     writer.writerow(test)

# print("Data appended to CSV:", csv_file)


def print_cards(code, list):
    print(code)
    URL = 'https://masshealth.ehs.state.ma.us/ProviderDirectory/Home/BehaviorSearchAsync?distance=5&accessiable=false&location=' + code + '&ProviderType=32&Page=0'
    
    req = requests.get(URL)

    json_str = json.loads(req.content)

    total_results = json_str['TotalResults']
    pages = int(total_results/6)
    pages = math.ceil(pages)

    for page in range(pages):
        URL = 'https://masshealth.ehs.state.ma.us/ProviderDirectory/Home/BehaviorSearchAsync?distance=5&accessiable=false&location=' + code + '&ProviderType=32&Page=' + str(page)
        req = requests.get(URL)
        json_str = json.loads(req.content)
        for result in json_str["Results"]:
            if result:
                result_dict = {
                        "Name": result["Name"],
                        "Address": result["Address1"],
                        "City": result["City"],
                        "State": result["State"],
                        "Zip Code": result["Zip"],
                        "Phone": result["Phone"],
                        "Health Plans": result["HealthPlans"],
                        "Specialties": result["Specialties"],
                }
                list.append(result_dict)

def main():
    zips = ['02537', '02538', '02539', '02540', '02541', '02542', '02543', '02552', '02553', '02554', '02556', '02557', '02558', '02559', '02561', '02562', '02563', '02564', '02568', '02571', '02574', '02575', '02576', '02584', '02601', '02630', '02631', '02632', '02633', '02634', '02635', '02637', '02638', '02639', '02641', '02642', '02643', '02644', '02645', '02646', '02647', '02648', '02649', '02650', '02651', '02652', '02653', '02655', '02657', '02659', '02660', '02661', '02662', '02663', '02664', '02666', '02667', '02668', '02669', '02670', '02671', '02672', '02673', '02675', '02702', '02703', '02712', '02713', '02714', '02715', '02717', '02718', '02719', '02720', '02721', '02722', '02723', '02724', '02725', '02726', '02738', '02739', '02740', '02741', '02742', '02743', '02744', '02745', '02746', '02747', '02748', '02760', '02761', '02762', '02763', '02764', '02766', '02767', '02768', '02769', '02770', '02771', '02777', '02779', '02780', '02790', '02791', '05501']
    results_list = []

    field_names = ["Name", "Address", "City", "State", "Zip Code", "Phone", "Health Plans", "Specialties"]

    output_csv_file = "opht_data.csv"

    for zip in zips: 
        print_cards(zip, results_list)
        
    with open(output_csv_file, 'a', newline='') as f:
        writer = csv.DictWriter(f, field_names)

        for entry in results_list:
            writer.writerow(entry)

main()