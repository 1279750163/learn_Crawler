import requests
from bs4 import BeautifulSoup

def get_novel_chapters():
    root_url = "https://www.biqiugexx.com/book_4070/"
    r = requests.get(root_url)
    r.encoding = "gbk"
    print(r.status_code)
    soup = BeautifulSoup(r.text, "html.parser")

    data = []
    for dd in soup.find_all("dd"):
        link = dd.find("a")
        if not link:
            continue

        data.append(("https://www.biqiugexx.com/book_4070%s" %link["href"], link.get_text()))

    return data


def get_chapter_content(url):
    r = requests.get(url)
    r.encoding = "gbk"
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.find("div", id='content').get_text()

if __name__ == '__main__':
    for chapter in get_novel_chapters():
        url, title = chapter
        with open("%s.txt" %title, "w", encoding="utf-8") as fout:
            fout.write(get_chapter_content(url))
        break


