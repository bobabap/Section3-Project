import math
from tqdm import trange
from .util import get_soup

review_url_form = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code={}&order=newest&page={}&onlySpoilerPointYn={}'


def calc_max_page(url, end_page):
    max_page = min(end_page, get_max_page(url))
    return max_page if max_page > 0 else False


def get_review_data(movie_id, start_page=1, end_page=-1, spoiler='N'):
    url = review_url_form.format(movie_id, start_page, spoiler)
    max_page = calc_max_page(url, end_page)

    if max_page == False:
        return "Failed: please check end_page"

    comments = []
    for page in trange(start_page, max_page + 1):
        url = review_url_form.format(movie_id, page, spoiler)
        current_page_comments = get_a_page(get_soup(url))
        comments += current_page_comments
    return comments


def remove_formal_text(text):
    if text[:4] == '관람객\n':
        return text[4:].strip()
    return text


def get_score(row):
    score = int(row.select('div[class=star_score] em')[0].text.strip())
    return score


def get_text(row):
    text = row.select('div[class=score_reple] p')[0].text.strip()
    return text


def get_user_id(row):
    user_id = row.select('div[class=score_reple] em')[0].text.strip()
    return user_id


def return_comment_form(score, text, user_id):
    comment = {'score': score,
               'text': text,
               'user': user_id
               }
    return comment


def get_a_page(soup):
    comments = []
    for row in soup.select('div[class=score_result] li'):
        try:
            score = get_score(row)
            text = get_text(row)
            user_id = get_user_id(row)
            text = remove_formal_text(text)
            comments.append(return_comment_form(score, text, user_id))
        except Exception as e:
            return e
            continue
    return comments


def get_max_page(url):
    soup = get_soup(url)
    try:
        num_comments = int(soup.select(
            'div[class="score_total"] em')[-1].text.replace(',', ''))
        return math.ceil(num_comments / 10)
    except Exception as e:
        return -1
