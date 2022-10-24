#!/usr/bin/python3

import signal

# SIGINTシグナルを無視するように設定
# 第一引数にはハンドラを設定するシグナル番号（ここでは`signal.SIGINT`）
# 第二引数にはシグナルハンドラ（ここでは`signal.SIG_IGN`）

signal.signal(signal.SIGINT, signal.SIG_IGN)
while True:
    pass
