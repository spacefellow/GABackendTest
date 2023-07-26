import requests
from bs4 import BeautifulSoup


WEBSITE = "https://greenatom.ru"


def get_html(website: str) -> str:
    """
    Функция принимает url веб-страницы.
    В случае успеха возвращает html-страницу, иначе выдает ошибку.
    """
    headers = {
         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.75"}
    page = requests.get(website, headers=headers)
    if page.status_code != 200:
        raise requests.exceptions.RequestException
    return page.text


def get_numbers_tags(html: str) -> int:
    """
    Функция подсчета количества тегов.
    Принимает на вход html страницу.
    """
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find_all()
    num_tags, num_tags_attrs = 0, 0
    for tag in tags:
        if tag.attrs:
            num_tags_attrs += 1
        num_tags += 1
    return num_tags, num_tags_attrs


def main() -> None:
    """Главная функция."""
    try:
        html = get_html(WEBSITE)
        result = get_numbers_tags(html)
        print(f"Number of tags: {result[0]}")
        print(f"Number of tags with attrs: {result[1]}")
    except requests.exceptions.RequestException as error:
        print("Something went wrong.")


if __name__ == "__main__":
    main()
