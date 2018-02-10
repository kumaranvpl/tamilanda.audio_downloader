from  bs4 import BeautifulSoup
from tqdm import tqdm
from urllib.parse import urlparse

import fire
import os
import re
import requests


def crawl_tamilanda(album_url, save_dir=False):
    if not save_dir:
        save_dir = os.getcwd()
    album_html = requests.get(album_url)
    parsed_uri = urlparse(album_url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

    soup = BeautifulSoup(album_html.text, "html.parser")

    album_name = False
    song_urls = []

    for li in soup.find_all("small"):
        file_url = li.a.get('href').replace("file.php", "download.php")

        if not album_name:
            album_name = file_url.split("/")[-2]
        song_urls.append(domain+file_url)

    if not os.path.exists(save_dir+"/"+album_name):
        os.makedirs(save_dir+"/"+album_name)

    album_dir = save_dir+"/"+album_name

    print("Found " + str(len(song_urls)) + " songs")
    count = 0
    for song_url in song_urls:
        count += 1
        print(str(count) + ". " + song_url.split(".flac")[0].split("/")[-1])

    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    for song_url in song_urls:
        song_name = song_url.split("/")[-1].split("&")[0]
        song_url = song_url.replace(" ", "%20") # URL encode space

        song_path = album_dir+"/"+song_name
        wget_command = "wget -c '" + song_url + "' -O " + "'" + song_path + "'"

        os.system(wget_command)


def main():
    fire.Fire(crawl_tamilanda)

if __name__ == "__main__":
    main()
