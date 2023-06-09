import time
import os

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        time.sleep(1)
        seconds -= 1

    # 播放提示音
    os.system("say 'Attention! Your focus timer has ended.'")

# 倒计时25分钟
focus_timer(25)
