[목적]

- 넷플릭스, 왓챠 등등 많은 영화 추천 서비스 플랫폼들이 있습니다
어떤 추천 방식이 사용자의 만족을 이끌어 낼 수 있을까 고민하여 만들게 되었습니다.

어떤 추천 방식이 사용자의 만족을
이끌어 낼 수 있을까 고민하여 만들게 되었습니다.

[목표] 

'user_number', 'sword', 'movie_id', 'score', 'movie_title', 'genres’

특성들을

```python
def pearsonR(s1, s2):
    s1_c = s1 - s1.mean()
    s2_c = s2 - s2.mean()
    return np.sum(s1_c * s2_c) / np.sqrt(np.sum(s1_c ** 2) * np.sum(s2_c ** 2))
```

피어슨 상관계수를 이용해 
특정 영화를 본 유저의 추천이라는 제목으로 영화를 추천해준다.

[단계]

1. 네이버에서 영화 정보 크롤링
- user_number
- movie_title
- movie_number
- movie_score
- user_name

[결과]

웹사이트 구현은 완성하지 못했지만 좋아하는 영화를 입력했을 때

영화 5가지를 추천해준다.
