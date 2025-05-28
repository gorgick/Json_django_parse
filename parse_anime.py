import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('div', class_='material-content_32787').find_all(
        'div', class_='TextContent_text__BydqR TextContent_colorBg__kvJG3')
    for div in divs:
        try:
            studio = div.find_all('p')[0].text.split(':')[1].strip()
        except:
            studio = ''
        try:
            director = div.find_all('p')[1].text.split(':')[1].strip()
        except:
            director = ''
        try:
            genre = div.find_all('p')[2].text.split(':')[1].strip()
        except:
            genre = ''
        try:
            amount_series = div.find_all('p')[3].text.split(':')[1].strip()
        except:
            amount_series = ''
        data = {
            'studio': studio,
            'director': director,
            'genre': [genre],
            'amount_series': amount_series
        }
        print(data)


def main():
    url = 'https://www.igromania.ru/article/32787/top-anime-2025-goda-luchshie-novinki-kotoryie-mozhno-posmotret-uzhe-sejchas/'
    all_links = get_data(get_html(url))


if __name__ == '__main__':
    main()
