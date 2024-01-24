
# -*- coding: utf-8 -*-

# Text Style
ts_no_effect = 0
ts_bold = 1
ts_disable = 2
ts_negative = 3
ts_underline = 4
ts_reverse = 7
ts_invisible = 8
ts_strikethrough = 9

# Text Color
tc_default = 0
tc_black = 30
tc_red = 31
tc_green = 32
tc_yellow = 33
tc_blue = 34
tc_purple = 35
tc_cyan = 36
tc_white = 37
tc_grey = 90
tc_light_red = 91
tc_light_green = 92
tc_light_yellow = 93
tc_light_blue = 94
tc_light_purple = 95
tc_light_cyan = 96
tc_light_white = 97

# Background Color
bgc_black = 40
bgc_red = 41
bgc_green = 42
bgc_yellow = 43
bgc_blue = 44
bgc_purple = 45
bgc_cyan = 46
bgc_white = 47


def style_print(message: str, style: int = ts_no_effect, text: int = tc_default, background: int = bgc_black) -> None:
    prefix = f"\033[{style};{text};{background}m"
    reset = f"\033[{ts_no_effect};{tc_default};{bgc_black}m"  # \033[0;0;40m
    print(f"{prefix}{message}{reset}")
