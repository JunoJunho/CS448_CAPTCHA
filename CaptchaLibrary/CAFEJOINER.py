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
            isFound=ie.ClickHref('0','A','ī�� �����ϱ�')
        except Exception, e:
            print e
            result.append("ie.ClickHref�� �����߿� ���ظ� �޾ҽ��ϴ�.")
            continue
        else:
            #������ �� �� �ִ�.
            if isFound == True:
                if ie.GetDocumentText(0).find(u"ī�� ���Խ�û") is not -1:
                    print 'ī�� ������ �õ��մϴ�.'
                    #break
                elif ie.GetDocumentText(0).find(u"��������") is not -1:
                    result.append("����-���� ��� Ǯ �� ����")
                    #print '����-���� ��� Ǯ �� ����'
                    continue
                elif ie.GetDocumentText().find(u"�����") is not -1:
                    result.append("����-���� ���� ������")
                    #print '����-���� ���� ������'
                    continue
                elif ie.GetDocumentText(0).find(u"�Ǹ�Ȯ��") is not -1:
                    result.append("����-���̵� �Ǹ�Ȯ���� �ʿ���")
                    #print '����-���̵� �Ǹ�Ȯ���� �ʿ���'
                    continue
                #�ְ��� ����
                if ie.GetDocumentText(0).find(unicode('�ְ���','cp949')) is not -1:
                    result.append("�õ�-�ְ��� ������ ��������;")
            #�̹� ���Ե� ī��
            else:
                result.append("����-�̹� ���Ե� ī���Դϴ�.")
        time.sleep(1)
        #print 'passing the first part'
        
        soup = BeautifulSoup(ie.GetDocumentHTML(0))
        questions = soup.find('div', attrs={'class': 'reg_wrap'})
        #pdb.set_trace()
        try:
            questions = questions.find_all("dl")
        except:
            #result.append("-������� ���� �����Դϴ�.")
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
            if ie.GetDocumentText(0).find(u"���ȹ��ڸ� ��Ȯ�� �Է��ϼ̽��ϴ�.") == -1 :
                #in case its failed
                ie.ClickLink2("http://i1.daumcdn.net/cafeimg/top7/cafe/make/btn_refresh.gif", 0)
                time.sleep(1)
                PressKey(win32con.VK_BACK, 5)
            else:
                #only when successfully quit.
                break
        #ie.ClickLink(u'����', 0)
        time.sleep(1)
        result.append("����-������ �Ϸ��߽��ϴ�.")
        
    ie.Navigate('http://cafe.daum.net/_c21_/mycafelist_main#')
    #result messages
    for res in result:
        print res,
    #newline
    print ''
