"""점수와 안내 문구를 화면에 보여주는 클래스입니다."""

# =====================================================================
# 이 파일(scoreboard.py)은 무슨 역할을 할까요?
# ---------------------------------------------------------------------
# 경기장의 "점수판" 설계도예요. 점수를 기억하고, 화면에 글자로 보여줘요.
#
# 점수판이 할 줄 아는 일 (메서드)
#   __init__  : 양쪽 점수를 0으로 시작하고, 글꼴(폰트)을 준비해요.
#   add_point : 득점한 쪽 점수를 1점 올려요.
#   winner    : 승리 점수에 도달한 사람이 있는지 확인해요.
#   reset     : 점수를 다시 0 : 0으로 돌려요. (R 키 재시작 때 사용)
#   draw      : 점수, 조작법, 안내 문구를 화면에 그려요.
#
# 화면 배치 (가로 800픽셀 기준)
#   - 왼쪽 점수 : 화면의 1/4 지점 (x = 200 근처)
#   - 오른쪽 점수: 화면의 3/4 지점 (x = 600 근처)
#   - 조작법, 안내 문구: 가운데 (x = 400 근처)
# =====================================================================

import pygame

# 설정표에서 글자 크기, 색, 화면 가로 길이를 가져옵니다.
from constants import FONT_SIZE, GRAY, INFO_FONT_SIZE, SCREEN_WIDTH, WHITE


class Scoreboard:
    """왼쪽/오른쪽 점수와 조작 안내를 그립니다."""

    def __init__(self):
        # 경기 시작! 양쪽 모두 0점에서 출발해요.
        self.left_score = 0
        self.right_score = 0
        # 글꼴 준비: "malgun gothic"(맑은 고딕)은 윈도우에 기본으로 있는 한글 글꼴이에요.
        # 한글 글꼴을 쓰지 않으면 한글이 네모(□□)로 깨져 보일 수 있어요.
        # 쉼표로 여러 글꼴을 적으면 "앞에서부터 컴퓨터에 있는 첫 번째 글꼴"을 사용해요.
        #   맑은 고딕(윈도우) → 애플 SD 고딕 Neo(맥) → 나눔고딕 → Noto Sans CJK(리눅스)
        korean_fonts = "malgungothic,applesdgothicneo,nanumgothic,notosanscjkkr"
        self.font = pygame.font.SysFont(korean_fonts, FONT_SIZE, bold=True)  # 점수용 큰 굵은 글씨
        self.info_font = pygame.font.SysFont(korean_fonts, INFO_FONT_SIZE)   # 안내용 작은 글씨

    def add_point(self, side):
        """side가 'left'이면 왼쪽, 'right'이면 오른쪽 점수를 1점 올립니다."""
        # == 는 "같은지 비교"하는 기호예요. (= 하나는 "값을 넣는다"는 뜻이라 달라요!)
        if side == "left":
            self.left_score += 1    # 왼쪽 점수 1 증가
        elif side == "right":       # elif = else if, "그게 아니고 만약 ~라면"
            self.right_score += 1   # 오른쪽 점수 1 증가

    def winner(self, win_score):
        """이긴 쪽이 있으면 'left' 또는 'right'를, 아직이면 None을 돌려줍니다."""
        # >= : "크거나 같다". 승리 점수(5점) 이상이면 승리!
        if self.left_score >= win_score:
            return "left"
        if self.right_score >= win_score:
            return "right"
        # None: 파이썬에서 "아무것도 없음"을 뜻하는 특별한 값이에요.
        # 여기서는 "아직 승자가 없어요"라는 의미로 써요.
        # 참고) if 문에서 None은 False처럼 취급돼요. game.py에서 이 성질을 이용해요.
        return None

    def reset(self):
        """점수를 0으로 되돌립니다."""
        self.left_score = 0
        self.right_score = 0

    def draw(self, screen, message=""):
        """점수와 가운데 안내 문구를 그립니다."""
        # message="": 안내 문구를 안 넣으면 빈 글자("")를 기본값으로 써요.

        # 1) 점수 숫자를 "글자 그림"으로 만들어요.
        # render(글자, 부드럽게 처리할지, 색) → 글자가 그려진 작은 그림이 만들어져요.
        # str(): 숫자(3)를 글자("3")로 바꿔요. render는 글자만 받을 수 있거든요.
        left_text = self.font.render(str(self.left_score), True, WHITE)
        right_text = self.font.render(str(self.right_score), True, WHITE)

        # 2) 만든 글자 그림을 화면에 붙여요.
        # blit: 그림을 화면의 (x, y) 위치에 "붙이는" 함수예요. (스티커 붙이기 느낌)
        # 가운데 정렬 계산: "놓고 싶은 중심 x - 글자 너비의 절반"
        #   → 이렇게 해야 글자의 한가운데가 원하는 위치에 오게 돼요.
        screen.blit(left_text, (SCREEN_WIDTH // 4 - left_text.get_width() // 2, 20))   # 화면 1/4 지점, 위에서 20픽셀
        screen.blit(
            right_text,
            (SCREEN_WIDTH * 3 // 4 - right_text.get_width() // 2, 20),   # 화면 3/4 지점
        )

        # 3) 조작법 안내를 회색 작은 글씨로 가운데(위에서 80픽셀)에 표시해요.
        #    ↑ ↓ 화살표는 키보드에 없는 특수 문자예요.
        #    윈도우: 한글 상태에서 ㅁ + [한자] 키 → 목록에서 선택 / 맥: Control + Command + Space
        #    또는 유니코드 "\u2191"(↑), "\u2193"(↓) 로 써도 같아요.
        hint = self.info_font.render("왼쪽: W / S    오른쪽: ↑ / ↓    재시작: R", True, GRAY)
        screen.blit(hint, (SCREEN_WIDTH // 2 - hint.get_width() // 2, 80))

        # 4) 안내 문구(예: "왼쪽 플레이어 승리!")가 있을 때만 흰 글씨로 표시해요.
        # if message: 글자가 비어 있지 않으면 True, 빈 글자("")면 False로 취급돼요.
        if message:
            msg = self.info_font.render(message, True, WHITE)
            screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, 120))
