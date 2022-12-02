import json

import requests

url = "https://maimai.cn/sdk/web/content/get_list"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56",
    "cookie": "seid=s1669887566204; guid=GRMEGx0cBBsTHwQeHFYHGBsZGxIfGx4YG1YcHwQSGx4bBBoEHRobBU1ObwocGQQdGR8FQ1hLTEt5ChoEGgQaBB0aGwVPR0VYQmkKA0VBSU9tCk9BQ0YKBmZnfmJhAgocGQQdGR8FXkNhSE99T0ZaWmsKAx4cUgoRHhxEQ30KERoEGhsKfmQKWV1FTkRDfQIKGgQfBUtGRkNQRWc=; _buuid=a0aa05d9-b784-4e77-a5c9-01754b830ea2; maimai_pc_login_show_tooltip=1; gdxidpyhxdE=HaLaI%5C8Ck9jT0%2Fmk8x9R%2FECqSA41Mcpitn0Wivpva1f%2FG1xNXnB8cj8XpWsHXZGp1%2F59p9OLYxy9dErCxIQH4Amv6Bzt1pbTQzMHmGOfSpGU8v8h6EAso%2BKMZpvzin%2FreQrJWQslaKEubu1G6e1Tpap%5CHDdCQYzz4XZL9NsNw6TV0gf6%3A1669896997872; YD00198168557789%3AWM_NI=xP8aYLc039kR8aZz8ZjUuavw7teMayelXayPF%2FLxdBLKkKRJokwCR5Q7LQkvDxnyGXanL6KIxW%2BrJaQTRndtk227V8OO9wRd9LyPQOglnysZR68%2B6vU32K8I6rW2gQ7iVDI%3D; YD00198168557789%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee92e850a897b682b35dad968eb3d54e828b8bb1d170a28da6d1ea4bae90bdb8fc2af0fea7c3b92abc90f882dc48a1f0fddaea5afcbf969bbb52aa8bbb82f57df5acabaee473a7b49882fc5c86f18499e74a9095a5acd142adb5b9a4d13f93e984b2ea7e88a8a29ac654a3b284d7ca43bc89e593c96b938c9e8fe780a9eefed8d5348d91f798d170fb94b7b1d445a5b4a29af25292eaf8ccb57e97edfeacbb43f6ae99d3e65bf5b79aa5cc37e2a3; YD00198168557789%3AWM_TID=W%2FJQlQ9VImZEVUFQARKBIOH3llVnf4Cm; u=238392979; u.sig=u_7H5JzwtL9jvv7VYp1GYBpKR38; access_token=1.368eb71ee4e93033618db18a0f0aa421; access_token.sig=EiN0Z-Dbqx-Pt8dsfgeLETV4wg4; u=238392979; u.sig=u_7H5JzwtL9jvv7VYp1GYBpKR38; access_token=1.368eb71ee4e93033618db18a0f0aa421; access_token.sig=EiN0Z-Dbqx-Pt8dsfgeLETV4wg4; channel=www; channel.sig=tNJvAmArXf-qy3NgrB7afdGlanM; maimai_version=4.0.0; maimai_version.sig=kbniK4IntVXmJq6Vmvk3iHsSv-Y; session=eyJzZWNyZXQiOiJmZVBMQzZ3NlFFNFI0V2U0ZDltZHU1ekEiLCJ1IjoiMjM4MzkyOTc5IiwiX2V4cGlyZSI6MTY2OTk4MjU5NzE0MiwiX21heEFnZSI6ODY0MDAwMDB9; session.sig=hcXeNcppbBrSwxHMsLbRKk-hY5A; csrftoken=GCVpey0f-_mzDyTZYwAV2I_jqAbIHHByGWlM; biz:jobs:session=eyJ1IjoiMjM4MzkyOTc5IiwiYWNjZXNzX3Rva2VuIjoiMS4zNjhlYjcxZWU0ZTkzMDMzNjE4ZGIxOGEwZjBhYTQyMSIsInZlcnNpb24iOiI0LjAuMCIsIl9leHBpcmUiOjE2Njk5ODI2MDMwNTgsIl9tYXhBZ2UiOjg2NDAwMDAwfQ==",
    "x-csrf-token": "GCVpey0f-_mzDyTZYwAV2I_jqAbIHHByGWlM"
}

def craw_page(page_number):
    params = {
        "api": "gossip/v3/square",
        "u": "238392979",
        "page": page_number,
        "before_id": 0
    }

    resp = requests.get(url, params=params, headers=headers)
    # print(resp.status_code)
    # print(resp.text)
    data = json.loads(resp.text)
    datas = []
    for text in data["list"]:
        datas.append(text["text"])
    return datas

with open("脉脉结果.txt", "w", encoding="utf-8") as f:
    for page in range(1, 11):
        print("craw page", page)
        datas = craw_page(page)
        f.write("\n".join(datas) + "\n")

