import requests
from bs4 import BeautifulSoup
from task3 import get_html


WEBSITE = "https://ifconfig.me"


def get_ip_address(html: str) -> str:
    """
    Функция возращает публичный IP-адрес.
    Принимает на вход html страницу.
    """
    soup = BeautifulSoup(html, "html.parser")
    ip_address = soup.find("strong", id="ip_address").contents
    return ip_address[0]


def main() -> None:
    """Главная функция."""
    try:
        html = get_html(WEBSITE)
        ip_address = get_ip_address(html)
        print(f"Your ip_address: {ip_address}")
    except requests.exceptions.RequestException as error:
        print(error)


if __name__ == "__main__":
    main()
