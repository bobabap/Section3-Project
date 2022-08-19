import re
import math
from tqdm import trange
from bs4 import BeautifulSoup
from .util import get_soup, clean_text, request_get_soup


# code = 93756 <- 명량
review_url_form = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code={}&order=newest&page={}&onlySpoilerPointYn=N'


def calc_max_page(url, end_page):
    max_page = min(end_page, get_max_page(url))
    return max_page if max_page > 0 else False


def get_max_page(url):
    soup = request_get_soup(url)
    try:
        num_comments = int(soup.select('div[class="score_total"] em')[-1].text.replace(',', ''))
        return math.ceil(num_comments / 10)
    except Exception as e:
        return -1


def get_user_code(movie_id, start_page=1, end_page=-1):
    url = review_url_form.format(movie_id, start_page)
    max_page = calc_max_page(url, end_page)

    if max_page == False:
        return "Failed: please check end_page"

    comments = []
    for page in trange(start_page, max_page+1):
        url = review_url_form.format(movie_id, page)
        current_page_comments = get_a_page(get_soup(url))
        comments += (current_page_comments)
    return comments

def request_get_user_code(movie_id, start_page=1, end_page=-1):
    url = review_url_form.format(movie_id, start_page)
    max_page = calc_max_page(url, end_page)

    if max_page == False:
        return "Failed: please check end_page"

    comments = []
    for page in trange(start_page, max_page+1):
        url = review_url_form.format(movie_id, page)
        current_page_comments = get_a_page(request_get_soup(url))
        comments += (current_page_comments)
    return comments


def return_comment_form(user_id):
    comment = {
        'user': user_id
    }
    return comment


def get_a_page(soup):
    comments = []
    
    for row in soup.select('div[class=score_result] li'):
        try:
            user_id = get_user_id(row)
            comments.append(return_comment_form(user_id))
        except:
            pass
            continue
    return comments


def get_user_id(row):
    user_id = str(row.select('div[class=score_reple] em a')[0])
    return clean_text(user_id)


def clean_text(text):
    code = re.findall("\d+", text)
    return code[0]
