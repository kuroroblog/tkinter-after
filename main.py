import tkinter as tk
import time

class Application(tk.Frame):
    # hello worldを出力する関数
    # keyword : dict型
    def getHelloWorld(self, keyword):
        print(keyword['text'])
        # 5000ms後にself.getHelloWorld関数を実行
        # 第一引数 : どのくらい遅らせて第二引数を実行するのかを時間設定する(単位はミリ秒)。
        # 第二引数 : 第一引数経過後に実行する関数。self.getHelloWorldとする。
        # 第三引数(任意) : 関数実行時に渡される引数
        # 戻り値 : ID(after関数の設定情報に紐づくID)
        # self.master.after(5000, self.getHelloWorld, {
        #     "text" : "hello world",
        # })

    # after関数に関するサンプル関数
    def getAfterSample(self):
        # 5000ms後にself.getHelloWorld関数を実行
        # 第一引数 : どのくらい遅らせて第二引数を実行するのかを時間設定する(単位はミリ秒)。
        # 第二引数 : 第一引数経過後に実行する関数。self.getHelloWorldとする。
        # 第三引数(任意) : 関数実行時に渡される引数
        # 戻り値 : ID(after関数の設定情報に紐づくID)
        return self.master.after(5000, self.getHelloWorld, {
            "text" : "hello world",
        })

    # helloを出力する関数
    def getHello(self):
        # time.sleep(3)
        self.master.after(3000, self.getHello)
        print('hello')

    # time.sleepとafter関数を比較する関数
    def confirmTimeVsAfter(self):
        # Windowを親要素としてbutton Widgetを作成する。
        # command : ボタンをクリックした場合に、実行する関数を設定。self.getHelloとする。
        # text : テキスト情報
        # Buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        button = tk.Button(self.master, command=self.getHello, text='クリック')
        # Windowを親要素として、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        button.pack()

    # after関数をキャンセルする関数
    # id : after関数の設定情報に紐づくID
    def removeAfterSample(self, id):
        # 第一引数 : after関数の設定情報に紐づくID
        self.master.after_cancel(id)

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)
        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200+120+0")

        # id = self.getAfterSample()
        # self.removeAfterSample(id)
        self.confirmTimeVsAfter()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
