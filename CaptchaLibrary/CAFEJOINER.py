# -*- coding: cp949 -*-
import sys
import IEC
import time
import win32gui
import win32con
from WriteGuess import WriteGuessString, PressKey
from bs4 import BeautifulSoup

sys.path.append('./CaptchaLibrary/CHARACTERIZER')
from CHARACTERIZER import CHARACTERIZER as GUESSER
import pdb

#invariant: only if it's logged in!
def CAFEJOINER(ie, cafelist, Theta1, Theta2):
    #pdb.set_trace()
    for cafe in cafelist:
        result = []
        #result.append(cafe)
        ie.Navigate(cafe)

        time.sleep(5)
        try:
            #pdb.set_trace()
            isFound=ie.ClickHref('0','A','카페 가입하기')
        except Exception, e:
            print e
            result.append("ie.ClickHref을 실행중에 방해를 받았습니다.")
            continue
        else:
            #가입을 할 수 있다.
            if isFound == True:
                if ie.GetDocumentText(0).find(u"카페 가입신청") is not -1:
                    print '카페 가입을 시도합니다.'
                    #break
                elif ie.GetDocumentText(0).find(u"가입퀴즈") is not -1:
                    result.append("실패-가입 퀴즈를 풀 수 없음")
                    #print '실패-가입 퀴즈를 풀 수 없음'
                    continue
                elif ie.GetDocumentText().find(u"출생자") is not -1:
                    result.append("실패-가입 연령 미충족")
                    #print '실패-가입 연령 미충족'
                    continue
                elif ie.GetDocumentText(0).find(u"실명확인") is not -1:
                    result.append("실패-아이디 실명확인이 필요함")
                    #print '실패-아이디 실명확인이 필요함'
                    continue
                #주관식 여부
                if ie.GetDocumentText(0).find(unicode('주관식','cp949')) is not -1:
                    result.append("시도-주관식 문제가 섞여있음;")
            #이미 가입된 카페
            else:
                result.append("실패-이미 가입된 카페입니다.")
        time.sleep(1)
        #print 'passing the first part'
        
        soup = BeautifulSoup(ie.GetDocumentHTML(0))
        questions = soup.find('div', attrs={'class': 'reg_wrap'})
        #pdb.set_trace()
        try:
            questions = questions.find_all("dl")
        except:
            #result.append("-가입퀴즈가 없는 오류입니다.")
            ie.Navigate(cafe)
            continue

        PressKey(win32con.VK_HANGUL)
        PressKey(win32con.VK_TAB, 2)

        for i in range(len(questions)-3):
            WriteGuessString('dkfrpTdjdy')
            time.sleep(0.1)
            PressKey(win32con.VK_SPACE)
            time.sleep(0.1)
            PressKey(win32con.VK_TAB)
            time.sleep(0.1)
            
        PressKey(win32con.VK_HANGUL)
        while 1:
            try:
                guessSTR = GUESSER(Theta1, Theta2, "C:\TEST/1.jpg")
            except:
                result.append("Somehow GUESSER doesn't work")
                guessSTR = 'XXXXX'
            WriteGuessString(guessSTR)
            if ie.GetDocumentText(0).find(u"보안문자를 정확히 입력하셨습니다.") == -1 :
                #in case its failed
                ie.ClickLink2("http://i1.daumcdn.net/cafeimg/top7/cafe/make/btn_refresh.gif", 0)
                time.sleep(1)
                PressKey(win32con.VK_BACK, 5)
            else:
                #only when successfully quit.
                break
        #ie.ClickLink(u'가입', 0)
        time.sleep(1)
        result.append("성공-가입을 완료했습니다.")
        
    ie.Navigate('http://cafe.daum.net/_c21_/mycafelist_main#')
    #result messages
    for res in result:
        print res,
    #newline
    print ''
