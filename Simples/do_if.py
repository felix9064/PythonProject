#!/usr/bin/env python3
# -*- coding: utf-8 -*-

birth = int(input('请输入你的出生年份：'))
if birth >= 2000:
    print('你是00后')
elif birth >= 1990:
    print('你是90后')
elif birth >= 1980:
    print('你是80后')
elif birth >= 1970:
    print('你是70后')
elif birth >= 1960:
    print('你是60后')
else:
    print('你是60前')
