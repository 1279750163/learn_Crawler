url = "https://tianqi.2345.com/Pc/GetHistory"



headers = {
    "user-agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"""

}

import requests
import pandas as pd

def craw_table(year, month):
    params = {
        "areaInfo[areaId]": 54511,
        "areaInfo[areaType]": 2,
        "date[year]": year,
        "date[month]": month

    }
    resp = requests.get(url, headers=headers, params=params)
    data = resp.json()["data"]
    df = pd.read_html(data)[0]
    return df

df_list = []
for year in range(2011, 2022):
    for month in range(1, 13):
        print("爬取:", year, month)
        df = craw_table(year, month)
        df_list.append(df)

pd.concat(df_list).to_excel("北京10年天气数据.xlsx", index=False)