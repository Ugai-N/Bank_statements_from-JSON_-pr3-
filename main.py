import os
from utils.data_manage import load_data, extract_data, sort_list, format_date, mask_account

file = os.path.join('data', 'operations.json')
raw_list = load_data(file)
filtered_list = extract_data(raw_list)
sorted_list = sort_list(filtered_list)

for i in sorted_list:
    print(f'{format_date(i[0])} {i[1]}\n'
          f'{mask_account(i[2])} -> {mask_account(i[3])}\n'
          f'{i[4]} {i[5]}\n')
