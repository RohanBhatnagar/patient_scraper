import requests
import sys
from bs4 import BeautifulSoup
import numpy as np
import json
import math
import pandas as pd

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
                name = result["Name"]
                address = result["Address1"]
                city = result["City"]
                state = result["State"]
                zip_code = result["Zip"]
                phone = result["Phone"]
                latitude = result["Latitude"]
                longitude = result["Longitude"]
                distance = result["Distance"]
                health_plans = result["HealthPlans"]
                specialties = result["Specialties"]
                languages = result["Languages"]
                accommodations = result["Accommodations"]

                result_dict = {
                        "Name": result["Name"],
                        "Address": result["Address1"],
                        "City": result["City"],
                        "State": result["State"],
                        "Zip Code": result["Zip"],
                        "Phone": result["Phone"],
                        "Latitude": result["Latitude"],
                        "Longitude": result["Longitude"],
                        "Distance": result["Distance"],
                        "Health Plans": result["HealthPlans"],
                        "Specialties": result["Specialties"],
                        "Languages": result["Languages"],
                        "Accommodations": result["Accommodations"],
                }
                list.append(result_dict)

def main():

    start = 1001
    end = 5544
    step = 1
    arr = np.arange(start, end, step)
    zips = ['01001', '01002', '01003', '01004', '01005', '01007', '01008', '01009', '01010', '01011', '01012', '01013', '01014', '01020', '01021', '01022', '01026', '01027', '01028', '01029', '01030', '01031', '01032', '01033', '01034', '01035', '01036', '01037', '01038', '01039', '01040', '01041', '01050', '01053', '01054', '01056', '01057', '01059', '01060', '01061', '01062', '01062', '01063', '01066', '01068', '01069', '01070', '01071', '01072', '01073', '01074', '01075', '01077', '01079', '01080', '01081', '01082', '01083', '01084', '01085', '01086', '01088', '01089', '01090', '01092', '01093', '01094', '01095', '01096', '01097', '01098', '01101', '01102', '01103', '01104', '01105', '01106', '01107', '01108', '01109', '01111', '01115', '01116', '01118', '01119', '01128', '01129', '01138', '01139', '01144', '01151', '01152', '01199', '01201', '01202', '01203', '01220', '01222', '01223', '01224', '01225', '01226', '01227', '01229', '01230', '01235', '01236', '01237', '01238', '01240', '01242', '01243', '01244', '01245', '01247', '01252', '01253', '01254', '01255', '01256', '01257', '01258', '01259', '01260', '01262', '01263', '01264', '01266', '01267', '01270', '01301', '01302', '01330', '01331', '01337', '01338', '01339', '01340', '01341', '01342', '01343', '01344', '01346', '01347', '01349', '01350', '01351', '01354', '01355', '01360', '01364', '01366', '01367', '01368', '01370', '01373', '01375', '01376', '01378', '01379', '01380', '01420', '01430', '01431', '01432', '01434', '01436', '01438', '01440', '01441', '01450', '01451', '01452', '01453', '01460', '01462', '01463', '01464', '01467', '01468', '01469', '01472', '01473', '01474', '01475', '01501', '01503', '01504', '01505', '01506', '01507', '01508', '01509', '01510', '01515', '01516', '01518', '01519', '01520', '01521', '01522', '01523', '01524', '01525', '01526', '01527', '01529', '01531', '01532', '01534', '01535', '01536', '01537', '01538', '01540', '01541', '01542', '01543', '01545', '01546', '01550', '01560', '01561', '01562', '01564', '01566', '01568', '01569', '01570', '01571', '01581', '01583', '01585', '01586', '01588', '01590', '01601', '01602', '01603', '01604', '01605', '01606', '01607', '01608', '01609', '01610', '01611', '01612', '01613', '01614', '01615', '01653', '01655', '01701', '01702', '01703', '01704', '01705', '01718', '01719', '01720', '01721', '01730', '01731', '01740', '01741', '01742', '01745', '01746', '01747', '01748', '01749', '01752', '01754', '01756', '01757', '01760', '01770', '01772', '01773', '01775', '01776', '01778', '01784', '01801', '01803', '01805', '01810', '01812', '01813', '01815', '01821', '01822', '01824', '01826', '01827', '01830', '01831', '01832', '01833', '01834', '01835', '01840', '01841', '01842', '01843', '01844', '01845', '01850', '01851', '01852', '01853', '01854', '01860', '01862', '01863', '01864', '01865', '01866', '01867', '01876', '01879', '01880', '01885', '01886', '01887', '01888', '01889', '01890', '01899', '01901', '01902', '01903', '01904', '01905', '01906', '01907', '01908', '01910', '01913', '01915', '01921', '01922', '01923', '01929', '01930', '01931', '01936', '01937', '01938', '01940', '01944', '01945', '01949', '01950', '01951', '01952', '01960', '01961', '01965', '01966', '01969', '01970', '01971', '01982', '01983', '01984', '01985', '02018', '02019', '02020', '02021', '02025', '02026', '02027', '02030', '02032', '02035', '02038', '02040', '02041', '02043', '02044', '02045', '02047', '02048', '02050', '02051', '02052', '02053', '02054', '02055', '02056', '02059', '02060', '02061', '02062', '02065', '02066', '02067', '02070', '02071', '02072', '02081', '02090', '02093', '02108', '02109', '02110', '02111', '02112', '02113', '02114', '02115', '02116', '02117', '02118', '02119', '02120', '02121', '02122', '02123', '02124', '02125', '02126', '02127', '02128', '02129', '02130', '02131', '02132', '02133', '02134', '02135', '02136', '02137', '02138', '02139', '02140', '02141', '02142', '02143', '02144', '02145', '02148', '02149', '02150', '02151', '02152', '02153', '02155', '02156', '02163', '02169', '02170', '02171', '02176', '02180', '02184', '02185', '02186', '02187', '02188', '02189', '02190', '02191', '02196', '02199', '02201', '02203', '02204', '02205', '02206', '02210', '02211', '02212', '02215', '02217', '02222', '02238', '02241', '02269', '02283', '02284', '02293', '02297', '02298', '02301', '02302', '02303', '02304', '02305', '02322', '02324', '02325', '02327', '02330', '02331', '02332', '02333', '02334', '02337', '02338', '02339', '02341', '02343', '02344', '02345', '02346', '02347', '02348', '02349', '02350', '02351', '02355', '02356', '02357', '02358', '02359', '02360', '02361', '02362', '02364', '02366', '02367', '02368', '02370', '02375', '02379', '02381', '02382', '02420', '02421', '02445', '02446', '02447', '02451', '02452', '02453', '02454', '02455', '02456', '02457', '02458', '02459', '02460', '02461', '02462', '02464', '02465', '02466', '02467', '02468', '02471', '02472', '02474', '02475', '02476', '02477', '02478', '02479', '02481', '02482', '02492', '02493', '02494', '02495', '02532', '02534', '02535', '02536', '02537', '02538', '02539', '02540', '02541', '02542', '02543', '02552', '02553', '02554', '02556', '02557', '02558', '02559', '02561', '02562', '02563', '02564', '02568', '02571', '02574', '02575', '02576', '02584', '02601', '02630', '02631', '02632', '02633', '02634', '02635', '02637', '02638', '02639', '02641', '02642', '02643', '02644', '02645', '02646', '02647', '02648', '02649', '02650', '02651', '02652', '02653', '02655', '02657', '02659', '02660', '02661', '02662', '02663', '02664', '02666', '02667', '02668', '02669', '02670', '02671', '02672', '02673', '02675', '02702', '02703', '02712', '02713', '02714', '02715', '02717', '02718', '02719', '02720', '02721', '02722', '02723', '02724', '02725', '02726', '02738', '02739', '02740', '02741', '02742', '02743', '02744', '02745', '02746', '02747', '02748', '02760', '02761', '02762', '02763', '02764', '02766', '02767', '02768', '02769', '02770', '02771', '02777', '02779', '02780', '02790', '02791', '05501']
    results_list = []

    output_csv_file = "output_data.csv"
    df = pd.DataFrame(results_list)

    for zip in zips: 
        print_cards(zip, results_list)
        df.to_csv(output_csv_file, index=False)


main()