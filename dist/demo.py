#-*- coding: gbk -*-
from __future__ import unicode_literals
import requests
import itchat
import time

def get_news():
    url = "http://open.iciba.com/dsapi"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['translation']
    return contents, translation

def send_news():
    try:
        # ��½���΢���˺ţ��ᵯ����ҳ��ά�룬ɨ�輴��
        itchat.auto_login(hotReload=True)
        # ��ȡ���Ӧ�ĺ��ѱ�ע�������С����ֻ�Ǿٸ�����
        # �ĳ������İ����˵����֡�
        my_friend = itchat.search_friends(name=u'�½���')
        # ��ȡ��Ӧ���Ƶ�һ������
        XiaoMing = my_friend[0]["UserName"]
        # ��ȡ��ɽ�ֵ������
        message1 = str(get_news()[0])
        content = str(get_news()[1][17:])
        message2 = str(content)
        message3 = "�����������"
        # ������Ϣ
        itchat.send(message1, toUserName=XiaoMing)
        itchat.send(message2, toUserName=XiaoMing)
        itchat.send(message3, toUserName=XiaoMing)
        # ÿ86400�루1�죩������1�Σ�
        # ����linux�Ķ�ʱ��������Ϊÿ�ε�½����Ҫɨ���ά���½��
        # ���鷳��һ���£�������һֱ���Ű�
        # t = time(86400, send_news())
        # t.start()
    except:
        message4 = u"���������˳����� bug /(��o��)/~~"
        itchat.send(message4, toUserName=XiaoMing)

def main():
    send_news()

if __name__ == '__main__':
    main()