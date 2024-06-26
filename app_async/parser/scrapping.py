import aiohttp
import asyncio
from datetime import datetime
from typing import List, Dict, Any
from concurrent.futures import ThreadPoolExecutor

from app_async.parser.download_files import download_file
from app_async.parser.get_links import fetch_page, get_report_links
from app_async.utils.extract_xml import extract_report_data

BASE_URL = "https://spimex.com/markets/oil_products/trades/results/"


async def async_extract_report_data(file_path: str) -> List[Dict[str, Any]]:
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        return await loop.run_in_executor(pool, extract_report_data, file_path)


async def scrape_reports(
        start_page: int = 1, end_page: int = 10
) -> List[Dict[str, Any]]:
    """
    Сканирует отчеты с сайта и извлекает данные.

    :param start_page: Начальная страница для сканирования. По умолчанию 1.
    :param end_page: Конечная страница для сканирования. По умолчанию 365.
    :return: Список словарей с данными отчетов.
    """
    print("Starting report scraping...")

    download_tasks = []
    extract_tasks = []
    all_data = []
    link_date_map = {}

    async with aiohttp.ClientSession() as session:
        for page in range(start_page, end_page + 1):
            page_url = f"{BASE_URL}?page=page-{page}"
            page_html = await fetch_page(session, page_url)
            report_links_and_dates = await get_report_links(page_html)
            for link, date in report_links_and_dates:
                if date.year >= 2023:
                    link_date_map[link] = date
                    task = asyncio.create_task(download_file(session, link, date))
                    download_tasks.append(task)

        await asyncio.gather(*download_tasks)
        print("Extracting report data...")

        for link, date in link_date_map.items():
            file_path = f"downloads/{date}.xls"
            task = asyncio.create_task(async_extract_report_data(file_path))
            extract_tasks.append((task, date))

        for task, date in extract_tasks:
            report_data = await task
            for item in report_data:
                item["date"] = date
                item["created_on"] = datetime.now()
                item["updated_on"] = datetime.now()
            all_data.extend(report_data)

    return all_data
