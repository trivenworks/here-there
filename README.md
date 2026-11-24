# 여기저기 · GitHub 업로드용

서울의 소비·유동인구·정류장 승하차 자료로 20·30대 대상 팝업의 옥외광고 현장 조사 후보를 비교합니다.

| 파일 | 화면 |
| --- | --- |
| `index.html` | 홈 |
| `ad-candidates.html` | 스팟 비교 |
| `alternatives.html` | 광고 스팟 지도 |
| `dashboard.html` | 모델링 |
| `eda.html` | EDA |
| `insights.html` | 인사이트 |

## 업로드와 미리보기

이 폴더 안의 파일을 저장소 루트에 올립니다. 각 HTML에는 표시용 데이터, 글꼴, 이미지와 해당 보고서 PDF가 내장되어 있습니다. 정적 페이지는 HTML 파일을 브라우저에서 직접 열 수 있습니다.

로컬 서버 미리보기는 `./start.command`를 실행한 뒤 `http://localhost:8767/`에서 확인합니다. 기존 Vercel 설정은 `python3 scripts/build_static.py`로 정적 파일을 생성하고 `public/`을 사용합니다. 네이버 배경 지도에 연결하려면 로컬 `.env` 또는 배포 환경변수에 `NAVER_MAP_CLIENT_ID`를 설정합니다. 키가 없으면 내장 경계 지도로 표시됩니다.

원자료, 노트북, 학습 코드, 실제 환경변수, 빌드 결과 폴더는 배포본에 포함하지 않습니다.
