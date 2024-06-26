import requests
from datetime import datetime

from app_sync.parser.download_files import download_file
from app_sync.parser.get_links import fetch_page, get_report_links
from app_sync.utils.extract_xml import extract_report_data

BASE_URL = "https://spimex.com/markets/oil_products/trades/results/"


def scrape_reports(start_page=1, end_page=10):
    print("Starting report scraping...")

    all_data = []
    link_date_map = {}

    with requests.Session() as session:
        for page in range(start_page, end_page + 1):
            page_url = f"{BASE_URL}?page=page-{page}"
            page_html = fetch_page(session, page_url)
            report_links_and_dates = get_report_links(page_html)
            for link, date in report_links_and_dates:
                if date.year >= 2023:
                    link_date_map[link] = date
                    download_file(session, link, date)

        print("Extracting report data...")
        for link, date in link_date_map.items():
            file_path = f"downloads/{date}.xls"
            report_data = extract_report_data(file_path)
            for item in report_data:
                item["date"] = date
                item["created_on"] = datetime.now()
                item["updated_on"] = datetime.now()
            all_data.extend(report_data)

    return all_data