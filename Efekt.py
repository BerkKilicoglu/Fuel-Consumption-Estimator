# -*- coding: utf-8 -*-
import sys, os, re, time, socket, traceback
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtCore import QPropertyAnimation, QTimer, QSize,QEasingCurve
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QGraphicsOpacityEffect
class Effects():
    def __init__(self):
        super(Effects, self).__init__()
        self.utilsGlobal = None

    ANIMASYONLAR_TEMP = []
    def EFEKT_FadeOut(self, WIDGET, SURE=1000, GIZLE=False, FINISH_HOOK=None, VAL_MAX=0.99, VAL_MIN=0):
        try:
            if WIDGET == None:
                return
            EFEKT = QGraphicsOpacityEffect(WIDGET)
            WIDGET.setGraphicsEffect(EFEKT)
            ANIM = QPropertyAnimation(EFEKT, b"opacity")

            self.ANIMASYONLAR_TEMP.append(ANIM)
            ANIM.setDuration(SURE)
            if GIZLE == False:
                ANIM.setEndValue(VAL_MAX)
                ANIM.setStartValue(VAL_MIN)
            else:
                ANIM.setEndValue(VAL_MIN)
                ANIM.setStartValue(VAL_MAX)
            # ANIM.setEasingCurve(QEasingCurve.OutBack)
            if FINISH_HOOK != None:
                ANIM.finished.connect(FINISH_HOOK)
            else:
                def bitti():
                    WIDGET.setGraphicsEffect(None)

                ANIM.finished.connect(bitti)
            ANIM.start(QtCore.QAbstractAnimation.DeleteWhenStopped)



        except Exception as err:
            if self.utilsGlobal != None:
                self.utilsGlobal.Shared.hataKodGoster("Efekt Fade Out: %s" % str(err))
            else:
                self.hataKodGoster("Effects EFEKT_FadeOut: ")

    def hataKodGoster(self, err=""):# utilsglobal değeri none ise bunu kullansın
        exc_type, exc_obj, exc_tb = sys.exc_info()
        if exc_type == None and exc_obj == None and exc_tb == None:
            return
        fname = exc_tb.tb_frame.f_code.co_filename
        hataStr = "%s %s %s %s\nTraceback: %s" % (str(err), exc_type, fname, exc_tb.tb_lineno, traceback.format_exc())
        print(hataStr)
    def EFEKT_Shadow(self, WIDGET, RENK, RADIUS=9, OFFSET=0, OFFSET_Y=0, RET_EFFEKT=False):
        try:
            ef = QGraphicsDropShadowEffect()
            ef.setColor(RENK)
            ef.setBlurRadius(RADIUS)
            ef.setOffset(OFFSET)
            ef.setYOffset(OFFSET_Y)
            if not RET_EFFEKT:
                WIDGET.setGraphicsEffect(ef)
            else:
                self.ANIMASYONLAR_TEMP.append(ef)
                return ef
            self.ANIMASYONLAR_TEMP.append(ef)
        except Exception as err:
            self.utilsGlobal.Shared.hataKodGoster("Ayarlar Efekt Shadow: %s" % str(err))
    def EFEKT_Move(self, WIDGET, dX=0, dY=0, startX=None, startY=None, SURE=750, FINISH_HOOK=None, EasingCurve=QEasingCurve.OutCubic, PropertyName="pos"):
        try:
            ANIM = QPropertyAnimation(WIDGET, PropertyName.encode(),duration=SURE)
            self.ANIMASYONLAR_TEMP.append(ANIM)
            ANIM.setEasingCurve(EasingCurve)
            if startX == None and startY == None:
                if PropertyName == "pos":
                    ANIM.setStartValue(WIDGET.pos())
                else:
                    ANIM.setStartValue(WIDGET.size())
            else:
                if PropertyName == "pos":
                    p = WIDGET.pos()
                    if startX: p.setX(startX)
                    if startY: p.setY(startY)
                    ANIM.setStartValue(p)
                else:
                    p = WIDGET.size()
                    if startX: p.setWidth(startX)
                    if startY: p.setHeight(startY)
                    ANIM.setStartValue(p)

            if PropertyName == "pos":
                wp = WIDGET.pos()
                wp.setX(wp.x() + dX)
                wp.setY(wp.y() + dY)
                ANIM.setEndValue(wp)
            else:
                wp = WIDGET.size()

                wp.setWidth(wp.width() + dX)
                wp.setHeight(wp.height() + dY)
                ANIM.setEndValue(wp)
            # ANIM.setEasingCurve(QEasingCurve.OutBack)
            if FINISH_HOOK != None:
                ANIM.finished.connect(FINISH_HOOK)
            else:
                def bitti():
                    WIDGET.setGraphicsEffect(None)

                ANIM.finished.connect(bitti)
            #print("ANIM: start: ", ANIM.startValue(), " end: ", ANIM.endValue())
            ANIM.start(QtCore.QAbstractAnimation.DeleteWhenStopped)

        except Exception as err:

            if self.utilsGlobal != None:
                self.utilsGlobal.Shared.hataKodGoster("Efekt Move: %s" % str(err))
            else:
                print("Effects EFEKT_Move: ",str(err))

    class Efekt(object):
        Focus = False
        COUNT = 0


