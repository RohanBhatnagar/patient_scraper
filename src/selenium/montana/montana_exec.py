import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException
import re

src = ""
zips = ['59001', '59601', '59002', '59003', '59004', '59006', '59007', '59008', '59010', '59011', '59012', '59013', '59014', '59015', '59016', '59018', '59019', '59020', '59022', '59024', '59025', '59026', '59027', '59028', '59029', '59030', '59031', '59032', '59033', '59034', '59035', '59036', '59037', '59038', '59039', '59041', '59043', '59044', '59046', '59047', '59050', '59052', '59053', '59054', '59055', '59057', '59058', '59059', '59061', '59062', '59063', '59064', '59065', '59066', '59067', '59068', '59069', '59070', '59071', '59072', '59073', '59074', '59075', '59076', '59077', '59078', '59079', '59081', '59082', '59083', '59084', '59085', '59086', '59087', '59088', '59089', '59101', '59102', '59103', '59104', '59105', '59106', '59107', '59108', '59111', '59112', '59114', '59115', '59116', '59117', '59201', '59211', '59212', '59213', '59214', '59215', '59217', '59218', '59219', '59221', '59222', '59223', '59225', '59226', '59230', '59231', '59240', '59241', '59242', '59243', '59244', '59247', '59248', '59250', '59252', '59253', '59254', '59255', '59256', '59257', '59258', '59259', '59260', '59261', '59262', '59263', '59270', '59273', '59274', '59275', '59276', '59301', '59311', '59312', '59313', '59314', '59315', '59316', '59317', '59318', '59319', '59322', '59323', '59324', '59326', '59327', '59330', '59332', '59333', '59336', '59337', '59338', '59339', '59341', '59343', '59344', '59345', '59347', '59349', '59351', '59353', '59354', '59401', '59402', '59403', '59404', '59405', '59406', '59410', '59411', '59412', '59414', '59416', '59417', '59418', '59419', '59420', '59421', '59422', '59424', '59425', '59427', '59430', '59432', '59433', '59434', '59435', '59436', '59440', '59441', '59442', '59443', '59444', '59446', '59447', '59448', '59450', '59451', '59452', '59453', '59454', '59456', '59457',
        '59460', '59461', '59462', '59463', '59464', '59465', '59466', '59467', '59468', '59469', '59471', '59472', '59474', '59477', '59479', '59480', '59482', '59483', '59484', '59485', '59486', '59487', '59489', '59501', '59520', '59521', '59522', '59523', '59524', '59525', '59526', '59527', '59528', '59529', '59530', '59531', '59532', '59535', '59537', '59538', '59540', '59542', '59544', '59545', '59546', '59547', '59601', '59602', '59604', '59620', '59623', '59624', '59625', '59626', '59631', '59632', '59633', '59634', '59635', '59636', '59638', '59639', '59640', '59641', '59642', '59643', '59644', '59645', '59647', '59648', '59701', '59702', '59703', '59707', '59710', '59711', '59713', '59714', '59715', '59716', '59717', '59718', '59719', '59720', '59721', '59722', '59724', '59725', '59727', '59728', '59729', '59730', '59731', '59732', '59733', '59735', '59736', '59739', '59740', '59741', '59743', '59745', '59746', '59747', '59748', '59749', '59750', '59751', '59752', '59754', '59755', '59756', '59758', '59759', '59760', '59761', '59762', '59771', '59772', '59773', '59801', '59802', '59803', '59804', '59806', '59807', '59808', '59812', '59820', '59821', '59823', '59824', '59825', '59826', '59827', '59828', '59829', '59830', '59831', '59832', '59833', '59834', '59835', '59837', '59840', '59841', '59842', '59843', '59844', '59845', '59846', '59847', '59848', '59851', '59853', '59854', '59855', '59856', '59858', '59859', '59860', '59863', '59864', '59865', '59866', '59867', '59868', '59870', '59871', '59872', '59873', '59874', '59875', '59901', '59903', '59904', '59910', '59911', '59912', '59913', '59914', '59915', '59916', '59917', '59918', '59919', '59920', '59921', '59922', '59923', '59925', '59926', '59927', '59928', '59929', '59930', '59931', '59932', '59933', '59934', '59935', '59936', '59937']


def search(zip):
    zipcode = zip

    driver = webdriver.Chrome()

    driver.get(
        'https://mtdphhs-provider.optum.com/tpa-ap-web/?navDeepDive=MT_publicFindAProviderNew')
    driver.implicitly_wait(10)

    time.sleep(2)

    category = driver.find_element(by=By.ID, value='selectCategory')
    cDrop = Select(category)
    cDrop.select_by_value('20')

    specialty = driver.find_element(by=By.ID, value='specialtyCategory')
    sDrop = Select(specialty)
    sDrop.select_by_value('207W00000X')

    state = driver.find_element(by=By.ID, value='state')
    stDrop = Select(state)
    stDrop.select_by_value('MT')

    zip = driver.find_element(by=By.ID, value='zipCode')
    zip.send_keys(zipcode)

    find = driver.find_element(by=By.ID, value='findProviders')
    find.click()
    time.sleep(0.5)
    find.click()
    time.sleep(0.5)
    find.click()

    print("_______________________________________________________________")
    print(zipcode)
    print("_______________________________________________________________")

    try:
        table = driver.find_element(by=By.ID, value='providerResults')
        num_vis = driver.find_element(by=By.NAME, value='providerResults_length')
        nvDrop = Select(num_vis)
        nvDrop.select_by_value('100')
        time.sleep(0.5)
        for row in table.find_elements(by=By.TAG_NAME, value='tr'):
            for cell in row.find_elements(by=By.TAG_NAME, value='td'):
                hyperlink = cell.find_element(by=By.TAG_NAME, value='a')
                time.sleep(1)
                driver.execute_script("arguments[0].click()", hyperlink)
                print('--> ' + hyperlink.text)
                time.sleep(0.2)
                dtable = driver.find_element(by=By.ID, value='detailsTable1')
                detail_arr = []
                for drow in dtable.find_elements(by=By.TAG_NAME, value='tr'):
                    for dcell in drow.find_elements(by=By.TAG_NAME, value='td'):
                        detail_arr.append(dcell.text)
                extract_write(detail_arr)
    except NoSuchElementException:
        # class="paginate_button next"
        print("--> no results found")

    driver.quit()


def extract_write(arr):
    data = {
        "name": "NULL",
        "phone": "NULL",
        "24HourPhone": "NULL",
        "CareMgmtPhone": "NULL",
        "Fax": "NULL", 
        "Location": "NULL",
        "NPI/API": "NULL",
        "Specialty": "NULL",
        "Program": "NULL",
    }
    data["name"] = arr[0].replace(",", "")
    for i in range(0, len(arr), 1):
        if "24 Hour Office Phone #:\n" in arr[i]:
            data['24HourPhone'] = arr[i].replace("24 Hour Office Phone #:\n", "")
        elif "Phone #:\n" in arr[i]:
            data['phone'] = arr[i].replace("Phone #:\n", "")
        elif "Care Management Phone #:\n" in arr[i]:
            data['CareMgmtPhone'] = arr[i].replace("Care Management Phone #:\n", "")
        elif "Location:\n" in arr[i]:
            data['Location'] = arr[i].replace("Location:\n", "").replace("\n", "|")
        elif "NPI/API:\n: " in arr[i]:
            data['NPI/API'] = arr[i].replace("NPI/API:\n", "")
        elif "Specialties:\n" in arr[i]:
            data['Specialty'] = arr[i].replace("Specialties:\n", "")
        elif "Program Participation:\n" in arr[i]:
            data['Program'] = arr[i].replace("Program Participation:\n", "")
        elif "Fax #:\n" in arr[i]:
            data['Fax'] = arr[i].replace("Fax #:\n", "")

    print("----> extracted")

    csv_file_path = "./montana_ophts.csv"
    with open(csv_file_path, mode="a", newline='') as csvfile:
        fieldnames = data.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow(data)

    print("--------> data written to csv successfully!")

def main():
    for zip in zips: 
        search(zip)


main()


def remove_whitespace(text):
    text = text.strip()
    return re.sub(r'\s{2,}', ' ', text)
