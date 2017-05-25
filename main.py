from  bs4 import BeautifulSoup
from tqdm import tqdm
from urlparse import urlparse

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

    for li in soup.find_all(class_="collection-item avatar"):
        file_url = li.a.get('href').replace("filepc", "download")

        if not album_name:
            album_name = file_url.split("/")[-2]
        song_urls.append(domain+"/"+file_url)

    if not os.path.exists(save_dir+"/"+album_name):
        os.makedirs(save_dir+"/"+album_name)

    album_dir = save_dir+"/"+album_name

    print "Found " + `len(song_urls)` + " songs"
    count = 0
    for song_url in song_urls:
        count += 1
        print `count` + ". " + song_url.split(".flac")[0].split("/")[-1]

    for song_url in song_urls:
        song_name = song_url.split("/")[-1].split("&")[0]
        print "Downloading " + song_name

        r = requests.get(song_url, stream=True)

        # Total size in bytes.
        total_size = int(r.headers.get('content-length', 0))

        with open(album_dir+"/"+song_name, 'wb') as f:
            for data in tqdm(r.iter_content(32*1024), total=total_size, unit='B', unit_scale=True):
                f.write(data)

def main():
    fire.Fire(crawl_tamilanda)

if __name__ == "__main__":
    main()
