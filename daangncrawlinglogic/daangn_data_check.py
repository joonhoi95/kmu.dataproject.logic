import pandas as pd

from framework import fileHelper

item_list = ['아이폰', '에어팟', '노트북', '미니벨로', '갤럭시']

fileHelper.CeateFolder('data_week')


# 전체 파일 이름을 읽어와서 필터를 걸어줌
# 해당 파일이름으로 하나씩 CONCAT AND DUPLICATE
#csv_data_08.set_index('no_product', inplace=True) -> 2303개

'''

#csv_data_08 = pd.read_csv('data/' + '20221108_' + itemName + '_data_comp' + '.csv', encoding="utf-8-sig")
csv_data_14 = pd.read_csv('data/' + '20221114_' + itemName + '_data_comp' + '.csv', encoding="utf-8-sig")
csv_data_15 = pd.read_csv('data/' + '20221115_' + itemName + '_data_comp' + '.csv', encoding="utf-8-sig")
csv_data_16 = pd.read_csv('data/' + '20221116_' + itemName + '_data_comp' + '.csv', encoding="utf-8-sig")
csv_data_17 = pd.read_csv('data/' + '20221117_' + itemName + '_data_comp' + '.csv', encoding="utf-8-sig")
csv_data_19 = pd.read_csv('data/' + '20221119_' + itemName + '_data_comp' + '.csv', encoding="utf-8-sig")

df_dif_08_17 = pd.concat((csv_data_14, csv_data_15, csv_data_16, csv_data_17, csv_data_19))
df_drop_dif_08_17 = df_dif_08_17.drop_duplicates(['no_product'])

df_drop_dif_08_17.to_csv('data_week/' + itemName + '_data_1w.csv', encoding="utf-8-sig")

'''




