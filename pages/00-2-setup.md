## 파이썬 설치

1. [python.org](https://www.python.org/downloads/)에서 Python 3.10 이상을 내려받습니다.
2. 윈도우 설치 첫 화면에서 **Add python.exe to PATH**를 반드시 체크합니다.
3. 명령 프롬프트(터미널)에서 확인합니다.

```bash
python --version
```

## 편집기 고르기

| 편집기 | 장점 | 추천 대상 |
| --- | --- | --- |
| IDLE | 파이썬과 함께 설치, 가볍다 (F5 실행) | 1~12차시 텍스트 게임 |
| VS Code + Python 확장 | 자동 완성, 디버거, 터미널 내장 | 13차시 이후 핑퐁·프로젝트 |
| 웹 IDE (예: replit 등) | 설치 불필요 | 텍스트 게임 (pygame은 제한될 수 있음) |

※ 기억력 게임의 `print("\n" * 40)` 화면 지우기는 IDLE에서 스크롤하면 보일 수 있습니다.

## pygame 설치 (13차시부터)

```bash
pip install pygame
# 또는 핑퐁 폴더에서
pip install -r requirements.txt
# pip 명령이 안 되면
python -m pip install pygame
```

설치 확인:

```bash
python -c "import pygame; print(pygame.version.ver)"
```

## 자주 만나는 문제

| 증상 | 원인 | 해결 |
| --- | --- | --- |
| `'python'은(는) 내부 또는 외부 명령...` | PATH 미설정 | 재설치하며 PATH 체크, 또는 `py` 명령 사용 |
| `ModuleNotFoundError: No module named 'pygame'` | pygame 미설치 또는 다른 파이썬에 설치 | `python -m pip install pygame` |
| 핑퐁 한글이 □□로 보임 | 한글 글꼴 없음 | 맑은 고딕·애플SD고딕Neo·나눔고딕 중 하나 설치 (코드가 자동으로 찾음) |
| `ModuleNotFoundError: No module named 'game'` | 다른 폴더에서 실행 | 핑퐁 폴더로 이동(`cd`) 후 `python main.py` |
| ♥, ↑ 같은 기호를 어떻게 입력하지? | 키보드에 없는 특수 문자 | 한글 상태에서 ㅁ + 한자 키 (맥: Control + Command + Space), 또는 `"\u2665"`처럼 유니코드로 쓰기 (부록 06-5 참고) |
| 특수 문자가 □나 ?로 보임 | 편집기·터미널 글꼴 문제 | IDLE: Options → Configure IDLE에서 '맑은 고딕' 등으로 글꼴 변경 |
