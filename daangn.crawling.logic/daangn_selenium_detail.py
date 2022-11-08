#pip install beautifulsoup4

import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd

#data를 읽기
#추후에는 여러날의 data를 가져올텐데, 그때는 중복 data는 merge하여 data 저장
itemName = '아이폰'
csv_data = pd.read_csv('data/' + itemName + '.csv', encoding='CP949')

#컬럼 추가
csv_data['nm_user'] = np.NaN
csv_data['no_temperature'] = np.NaN
csv_data['dc_detail'] = np.NaN
csv_data['dc_count'] = np.NaN

#for문을 돌면서 해당 데이터 가져옴
for index in range(len(csv_data)):

    # main url 가져오기
    link = csv_data['dc_product_link'][index]
    response = requests.get(link)

    if response.status_code == 200:
        try:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            nm_user = soup.select_one('#nickname').text
            no_temperature = soup.select_one('#temperature-wrap > dd').text.replace(' ', '').replace('\n', '')
            dc_detail = soup.select_one('#article-detail').text
            dc_count = soup.select_one('#article-counts').text

            csv_data.loc[index, ['nm_user']] = nm_user
            csv_data.loc[index, ['no_temperature']] = no_temperature
            csv_data.loc[index, ['dc_detail']] = dc_detail
            csv_data.loc[index, ['dc_count']] = dc_count

        except:
            print(link[-8:])

    else:
        print(index, ':', response.status_code)

#작업이 완료됐다면 저장
csv_data.to_csv('data_comp.csv', encoding="utf-8-sig")




