from typing import Final

VERSION: Final[str] = "v0.1.0"  # 봇 버전
TEMPLATE_VERSION: Final[str] = "v1.4.1"  # 템플릿 버전
HELP_SELECT_RAW: Final[dict[str, str]] = {  # 간단한 명령어 설명(매개변수 미포함)
    "/가위바위보": "봇과 가위바위보 게임을 합니다.",
    "/도움말": "도움말을 출력합니다.",
    "/봇": "봇의 정보를 출력합니다.",
    "/주사위": "주사위를 굴립니다.",
    "/틱택토": "틱택토 게임을 합니다.",
    "/핑": "봇의 핑을 출력합니다.",
    "/홀짝": "홀짝 게임을 합니다."
}
HELP_EMBED_RAW: Final[dict[str, str]] = {  # 명령어 설명(매개변수 포함)
    "/가위바위보 [입력]": "봇과 가위바위보 게임을 합니다.",
    "/도움말": "도움말을 출력합니다.",
    "/봇": "봇의 정보를 출력합니다.",
    "/주사위 [범위1] (범위2)": "`[범위1]`~`(범위2)` 또는 1~`[범위1]` 범위 안에서 주사위를 굴립니다.",
    "/틱택토 [상대]": "`[상대]`와 틱택토 게임을 합니다, `[상대]`를 자신으로 설정해 연습할 수 있습니다.",
    "/핑": "봇의 핑을 출력합니다.",
    "/홀짝": "홀짝 게임을 합니다."
}
DATABASE_INIT: Final[list[dict[str, str | dict[str, str]]]] = [  # 데이터베이스 구조
]
OPTION_TYPES: Final[dict[int, str]] = {  # 슬래시 커맨드 옵션 타입
    1: "SUB_COMMAND",
    2: "SUB_COMMAND_GROUP",
    3: "STRING",
    4: "INTEGER",
    5: "BOOLEAN",
    6: "USER",
    7: "CHANNEL",
    8: "ROLE",
    9: "MENTIONABLE",
    10: "NUMBER",
    11: "ATTACHMENT"
}
