# Samil Digital본부 Git hub_portfolio
본 프로젝트는 ChatGPT의 코딩 보조를 활용해 웹 스크래핑 프로세스를 구현한 사례입니다.  
Gen AI의 응용 가능성을 실무적으로 실험하며, 비정형 데이터를 수집하고 시각화하는 워크플로우를 완성했습니다.
스크래핑 중 ChatGPT의 코드 제안에서 반복적으로 작동 오류가 발생했으며, CSS Selector를 직접 찾아 수정하여 정상 작동하도록 구현했습니다.

---

## 📁 프로젝트 구성

- `work1.py`: 금융위원회 보도자료 페이지를 크롤링하여 제목 수집
- `work2.py`: 명사 추출, 빈도 분석 및 워드클라우드 시각화 코드
- `금융위_보도자료_스크래핑.xlsx`: 수집된 보도자료 제목이 저장된 엑셀 파일

---

## 🛠 사용 기술

- Python 3.x
- Selenium, BeautifulSoup
- pandas, konlpy, wordcloud, matplotlib
- ChromeDriver

---

## 📊 분석 및 시각화

- `konlpy`의 `Okt`를 이용해 제목에서 명사를 추출
- 불용어 제거 후 2글자 이상 키워드를 대상으로 빈도수 분석
- `wordcloud`로 핵심 키워드 시각화

---

## 📝 실행 방법

1. 필요한 라이브러리 설치
    ```bash
    pip install -r requirements.txt
    ```

2. 보도자료 스크래핑
    ```bash
    python work2.py
    ```

3. 키워드 분석 및 시각화
    ```bash
    python keyword_analysis.py
    ```

---

## 📌 참고사항

- 워드클라우드를 위해 `C:/Windows/Fonts/malgun.ttf` 경로를 사용 (한글 폰트)
- 분석 대상: [금융위원회 보도자료](https://www.fsc.go.kr/no010102)
- 동적 로딩 대응을 위해 Selenium 사용

---

## 👤 작성자

- 지원자: [김예한]
- GitHub: [https://github.com/rkans32-jpg/work1](https://github.com/rkans32-jpg/work1)
