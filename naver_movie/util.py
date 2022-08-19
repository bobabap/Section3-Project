from bs4 import BeautifulSoup
import re
import urllib.request

import requests


def text_normalize(text):
    return text.strip()


# def get_soup(target_url):
#     html = urllib.request.urlopen(target_url).read()
#     soup = BeautifulSoup(html, 'html.parser')
#     return soup

def get_soup(target_url):
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
    html = requests.get(target_url, headers=header).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def clean_text(text):
    code = re.findall("\d+", text)
    return code[0]
