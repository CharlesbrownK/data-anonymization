import csv
import os.path
from csv import writer
from utils import publicKeyCipherEncrypt, publicKeyCipherDecrypt

content = []
csv_file_name = 'user_information'
path = f'./data/{csv_file_name}.csv'
with open(path, 'r', encoding='cp949') as file:
    informationFile = csv.reader(file)
    for row in informationFile:
        content.append(row)

file = f'./data/anonymization_{csv_file_name}.csv'
if os.path.exists(file):
    print('\n\033[31m \033[1m' + 'Warning: ' + '\033[0m' + f"The \033[92m{csv_file_name}\033[0m is exist in \033[92m.\data\{csv_file_name}.csv\033[0m! Please remove it or run this code in other places!\n")
else:
    index = content[0].index('Name')
    for i in range(1, len(content)):
        content[i][index] = publicKeyCipherEncrypt.main(content[i][index])
    
    print('\nFinish Encrypt All Name!')
    
    with open(file, 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        for i in range(len(content)):
            writer_object.writerow(content[i])
        f_object.close()
    print('\nComplete to anonymize data!\n')