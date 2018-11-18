# -*- coding:utf-8 -*-
__date__ = '2018/11/18 12:00'

import  win32com.client  #导入系统客户端库
speaker=win32com.client.Dispatch("SAPI.SPVOICE")#使用接口
speaker.Speak("语音分析，今日练习")#实现接口调用





