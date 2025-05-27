import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('div', class_='material-content_32787').find_all(
        'div', class_='TextContent_text__BydqR TextContent_colorBg__kvJG3')
    print(divs)


def main():
    url = 'https://www.igromania.ru/article/32787/top-anime-2025-goda-luchshie-novinki-kotoryie-mozhno-posmotret-uzhe-sejchas/'
    all_links = get_data(get_html(url))



if __name__ == '__main__':
    main()