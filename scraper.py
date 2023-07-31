import requests
import sys
from bs4 import BeautifulSoup
import numpy as np
import json
import math
import pandas as pd
import csv

def print_cards(code, list):
    print(code)
    URL = 'https://masshealth.ehs.state.ma.us/ProviderDirectory/Home/BehaviorSearchAsync?distance=5&accessiable=false&location=' + code + '&ProviderType=34&Page=0'
    
    req = requests.get(URL)

    json_str = json.loads(req.content)

    total_results = json_str['TotalResults']
    pages = int(total_results/6)
    pages = math.ceil(pages)

    for page in range(pages):
        URL = 'https://masshealth.ehs.state.ma.us/ProviderDirectory/Home/BehaviorSearchAsync?distance=5&accessiable=false&location=' + code + '&ProviderType=34&Page=' + str(page)
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
    zips = ['02655', '02657', '02659', '02660', '02661', '02662', '02663', '02664', '02666', '02667', '02668', '02669', '02670', '02671', '02672', '02673', '02675', '02702', '02703', '02712', '02713', '02714', '02715', '02717', '02718', '02719', '02720', '02721', '02722', '02723', '02724', '02725', '02726', '02738', '02739', '02740', '02741', '02742', '02743', '02744', '02745', '02746', '02747', '02748', '02760', '02761', '02762', '02763', '02764', '02766', '02767', '02768', '02769', '02770', '02771', '02777', '02779', '02780', '02790', '02791', '05501']
    results_list = []

    field_names = ["Name", "Address", "City", "State", "Zip Code", "Phone", "Health Plans", "Specialties"]

    output_csv_file = "output_data.csv"

    for zip in zips: 
        print_cards(zip, results_list)
        
    with open(output_csv_file, 'a', newline='') as f:
        writer = csv.DictWriter(f, field_names)

        for entry in results_list:
            writer.writerow(entry)

main()