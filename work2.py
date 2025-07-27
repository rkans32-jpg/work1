
import pandas as pd
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 1. 엑셀 파일 불러오기
df = pd.read_excel("금융위_보도자료_스크래핑.xlsx")
texts = df['제목'].dropna().astype(str).tolist()

# 2. Okt로 명사 추출
okt = Okt()
nouns = []
for sentence in texts:
    nouns += okt.nouns(sentence)

# 3. 불용어 제거 + 2자 이상 단어만
stopwords = set([
    "것", "수", "등", "이", "의", "에", "를", "은", "는", "가", "으로", "및",
    "대한", "있습니다", "관련", "보도", "자료","한국","제하","대해","정부","기사","유예", "위해", "기자", "내용", "설명", "확정"
])
filtered = [word for word in nouns if len(word) > 1 and word not in stopwords]

# 4. 빈도수 계산
word_counts = Counter(filtered)
top_words = word_counts.most_common(30)

# 5. 워드클라우드 생성
wc = WordCloud(
    font_path='C:/Windows/Fonts/malgun.ttf',
    background_color='white',
    width=800,
    height=400
).generate_from_frequencies(dict(top_words))

# 6. 시각화
plt.figure(figsize=(10, 6))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
plt.show()
