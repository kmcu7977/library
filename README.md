# 도서관 인수인계 게시판

근로장학생 층별 인수인계 체크리스트. GitHub Pages: https://kmcu7977.github.io/library/

## 구조
- `index.html` — 층 선택(2/3/4층) → `board.html?floor=N`
- `board.html` — 목록/항목/상세 3단 체크리스트(드래그 정렬, 우클릭 수정·삭제) + 공지사항(층별 편집) + 시간표(이미지 업로드) + 민원정리(날짜·학번·이름·비고 표)
- `style.css`, `시간표.png`(기본 이미지)

## 데이터 (Firebase Realtime Database `library-checklist-4ec86`)
| 경로 | 내용 |
|---|---|
| `checklists/floorN` | 층별 체크리스트 |
| `notices/floorN` | 층별 공지 |
| `timetable.imageBase64` | 시간표 이미지 |
| `complaints` | 민원정리 (전 층 공유) |

페이지 로드는 읽기만 하고, 저장은 사용자가 편집할 때만 일어난다.

## 배포
`main`에 push하면 GitHub Pages가 자동 반영(약 1분).

## 남은 일
- [ ] 민원정리 정렬·검색·엑셀 내보내기 (행이 많아지면)
