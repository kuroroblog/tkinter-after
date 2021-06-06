import tkinter as tk
import time

class Application(tk.Frame):
    # hello worldを出力する関数
    # keyword : dict型
    def getHelloWorld(self, keyword):
        print(keyword['text'])
        # self.master.after(5000, self.getHelloWorld, {
        #     "text" : "hello world",
        # })

    # after関数に関するサンプル関数
    def getAfterSample(self):
        # 5000ms後にgetHelloWorld関数を実行
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
        button = tk.Button(command=self.getHello)
        button.pack()

    # after関数をキャンセルする関数
    # id : after関数に紐づくid
    def removeAfterSample(self, id):
        self.master.after_cancel(id)

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)
        # アプリ画面(Window)の位置、大きさを設定する。
        self.master.geometry("300x200+120+0")

        # while True:
        #     self.getAfterSample()
        # id = self.getAfterSample()
        # self.removeAfterSample(id)

        self.confirmTimeVsAfter()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    app.mainloop()
