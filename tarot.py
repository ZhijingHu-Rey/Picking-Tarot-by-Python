
import random

import os


LANGUAGE_CN = 0
LANGUAGE = LANGUAGE_CN

try:
    import matplotlib.pyplot as plt
    import matplotlib.pyplot as plt

except:
    print ('读取文件错误！！')
    os.system('pip install matplotlib')
    import matplotlib.pyplot as plt
    import matplotlib.pyplot as plt


BIG_CARD_CN = ["愚者","魔术师","女祭司","女皇","皇帝","教皇","恋人","战车","力量","隐者","命运之轮","正义","倒吊人","死神","节制","恶魔","塔","星星","月亮","太阳","审判","世界"]

UPSIDEDOWN_CN = ["正位","逆位"]

SMALL_CARD_TYPE_CN = ["权杖","星币","圣杯","宝剑"]


SMALL_CARD_CN = ["国王","王后","骑士","侍卫","十","九","八","七","六","五","四","三","二","一"]


if __name__ == '__main__':
    if LANGUAGE == LANGUAGE_CN:
        print("请静下心来，在心中仔细思考你想要提问的问题，心诚则灵")
        print("随意在键盘上输入你心中想到的数字，或者输入 q 以结束进程")
        print("在输入完成后按下回车")
    FIRST_TIME = True
    while True:
        inStr = input()
        if inStr == "q":
            break
        sun = 0
        for wd in inStr:
            sun = (sun + ord(wd)*random.randint(0,155))%156
        ans = sun
        card = ""
        cardName = ""
        positiveCard = ans%2
        ans = int(ans / 2)
        if ans < 22:
            card = "maj_" + "%02d" % ans
            if LANGUAGE == LANGUAGE_CN:
                cardName = BIG_CARD_CN[ans] + " - " + UPSIDEDOWN_CN[positiveCard]
        else:
            mNum = ans - 22
            small_type = int(mNum/14)
            small_card = mNum-14*int(mNum/14)
            card = "min_" +  "_"
            if LANGUAGE == LANGUAGE_CN:
                cardName = SMALL_CARD_TYPE_CN[small_type]+SMALL_CARD_CN[small_card] + " - " + UPSIDEDOWN_CN[positiveCard]

        print("\n" + cardName + "\n")

        if LANGUAGE == LANGUAGE_CN:
            print("如果想要继续，请继续输入任意文字；如果想要离开，按 q 结束进程")


