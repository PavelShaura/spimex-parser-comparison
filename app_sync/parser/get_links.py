from bs4 import BeautifulSoup
from datetime import datetime
import requests


def fetch_page(session, url):
    print(f"Fetching page: {url}")
    response = session.get(url)
    return response.text


def get_report_links(page_html):
    print("Extracting report links and dates...")
    soup = BeautifulSoup(page_html, "html.parser")
    report_links = []
    dates = []
    for item in soup.select(".accordeon-inner__wrap-item"):
        link = item.select_one(".accordeon-inner__item-title.link.xls")
        if link:
            report_links.append("https://spimex.com" + link.get("href"))
        date_elem = item.select_one(".accordeon-inner__item-inner__title span")
        if date_elem:
            date_str = date_elem.text.strip()
            dates.append(datetime.strptime(date_str, "%d.%m.%Y").date())
    return list(zip(report_links, dates))