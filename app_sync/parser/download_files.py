import os
import requests


def download_file(session, url, date, folder="downloads"):
    os.makedirs(folder, exist_ok=True)
    filename = f"{folder}/{date}.xls"
    print(f"Downloading file: {filename} from {url}")

    response = session.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Successfully downloaded {filename}")
    else:
        print(f"Failed to download {url}: HTTP {response.status_code}")