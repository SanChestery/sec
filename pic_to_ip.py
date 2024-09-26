'''
Author:         Yann Santschi
Version:        1.0
Description:    OCR extraction of IPs from pictures
Output:         Deduplicated list of IPs from pictures in the folder
'''

import cv2
import easyocr
import re
import os

folder_path = r'PATH'
ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
ip_addresses = []


def img_2_text(location):
    img = cv2.imread(location)
    reader = easyocr.Reader(['en'], gpu=False)
    text = reader.readtext(img)
    print(text)

    # Loop through the list and search for IP addresses in the second element of each tuple
    for item in text:
        string_data = item[1]  # Second element of each tuple
        match = re.search(ipv4_pattern, string_data)
        if match:
            ip_addresses.append(match.group())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            file = os.path.join(folder_path, filename)
            img_2_text(file)

    unique_ip_addresses = list(set(ip_addresses))

    with open('extracted_ips.txt', 'w') as out_file:
        for ip in unique_ip_addresses:
            out_file.write(ip + '\n')

