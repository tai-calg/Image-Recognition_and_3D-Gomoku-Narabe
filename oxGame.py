# coding: UTF-8
# coding: Shift_JIS
import numpy as np 
import PySimpleGUI as sg
import logging as log
class InputMark():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        #self.nowPlay = 0

    def WriteError(self):
        print("Error! 1~4の値を代入してください。例：1 3")

    def InputXY(self):
        flag = False
        while flag == False:
            wherePoint = input("半角空白で区切って置く場所を決めてください。順序はx,yです。")
            if wherePoint == "exit":
                flag = True
            if " " not in wherePoint:
                self.WriteError()  #クラス内の関数を呼び出したいならself.関数名とする（その関数の方にも引数selfを入れておくこと）
                continue
            
            self.x = wherePoint.split(" ")[0]
            self.y = wherePoint.split(" ")[1]
            
            if self.x not in ["1","2","3","4"]:
                self.WriteError()
                continue
            if self.y not in ["1","2","3","4"]:
                self.WriteError()
                continue

            self.x = int(self.x)
            self.y = int(self.y)
            
            if self.board[-(self.y -1+1)][self.x -1] in [1,2]: #重複をさせなくする
                print("既にマークが付いています、別の箇所を選択してください")
                continue

            if 0 < self.x  <= 4 and 0 < self.y <= 4:
                flag = True
            else:
                self.WriteError()
                continue
    
    def PlayerSet(self):
        self.player1 = str(input("一人目のプレイヤーの名前を入力してください:"))
        print(f"{self.player1}さんの記号は●です")

        self.player2 = str(input("二人目のプレイヤーの名前を入力してください:"))
        print(f"{self.player2}さんの記号は✖です")

        self.playerList = [self.player1, self.player2]




class App(InputMark):
    #bingo = False bingoはフラグではあるが定数ではないのでinitのなかに入れる（クラス変数の役割ではない）
    #board = [] ここは予想通りいらなかった

    def __init__(self, x=1, y=1):
        super().__init__(x,y)
        self.nowPlay = 0
        self.bingo = False
        self.count = 0
        #self.board = board # ここCreateBoardがやってくれるからいらない。init以外のところでself.定義してもいい
        """
        initでself設定するのはインスタンス定義の時に毎回初期化したい変数だけ（ここに入れておかないと二つ目のインスタンス
        を作った時に一つ目のインスタンスの変数を引き継いでしまう。）
        引数にnowPlayを入れていないが、self.nowPlay = 1とはしている。このことでインスタンス生成時に毎回定義するのは面倒だか         らしたくないが、毎回初期化はしたいという要望を叶えられる。
        """
        
    def CreateBoard(self):
        BC = [0,0,0,0]
        board = [] #盤面の設計
        for i in range(len(BC)): # n*nの盤面を作る
            board.append(BC)
        #self.board3D =[board,board,board] #3次元に
        #self.board3D = np.array(board3D)
        self.board = np.array(board)
        
        self.userboard = self.board.copy() #ユーザーから見るボード



    def Switch(self):
        self.oxList = ["●","✖️"]
        print("プレイヤーが切り替わります。")
        print(f"次は{self.playerList[self.nowPlay]}さんの番です")
        if self.nowPlay == 0:
            self.marubatu = self.oxList[0]
            self.plot = 1
            self.nowPlay = 1 #nowPlayをここで変えているが、本当に変わるのはPlotMarkメソッドを実行したあと

        elif self.nowPlay == 1:
            self.marubatu = self.oxList[1]
            self.nowPlay = 0
            self.plot = 2


    def PlotMark(self):
        
        self.board[-(self.y -1+1)][self.x -1]= self.plot 
        # 入力した座標をデカルト座標系と一致させる,更新するのはバックエンドのボードのみ！

        if type(self.userboard) != list:
            self.userboard = self.userboard.tolist()
        for row_num in range(len(self.userboard)):
            for col_num in range(4):
                if self.board[row_num][col_num] == 0 :
                    self.userboard[row_num][col_num] = "□"      #空白部分は□で表示
                    
                elif self.board[row_num][col_num] == self.plot :
                    self.userboard[row_num][col_num] = self.marubatu # ここでユーザー側ボードと同期

        for i in self.userboard:
            print(i)
        print("=========================")


        # 一列揃うとビンゴの表示をしてくれる関数を作ろう
    def RowBingo(self):
            for i in range(4):
                if self.userboard[i][0] == self.marubatu and self.userboard[i][1] == self.marubatu \
                and self.userboard[i][2] == self.marubatu and self.userboard[i][3] == self.marubatu:
                    print(f"ビンゴ！y={4-i}で揃った！") #0+4=4,i+j=4となるように別の関数で作っておく
                    print(f"決着！　{self.playerList[self.nowPlay -1]}さんの勝利です！")
                    self.bingo =True # 混乱を避けるために、self.bingoではなく、クラス.クラス変数とした方が無難。
    def ColBingo(self):
            for i in range(4):
                if self.userboard[0][i] == self.marubatu and self.userboard[1][i] == self.marubatu \
                and self.userboard[2][i] == self.marubatu and self.userboard[3][i] == self.marubatu:
                    print(f"ビンゴ！x={i+1}で揃った！")
                    self.bingo =True
                    print(f"決着！　{self.playerList[self.nowPlay -1]}さんの勝利です！")
    def DiagonalBingo(self):
            if self.userboard[0][0] == self.marubatu and self.userboard[1][1] == self.marubatu \
            and self.userboard[2][2] == self.marubatu and self.userboard[3][3] == self.marubatu:

                print(f"ビンゴ！ y=-xで揃った！")
                self.bingo = True
                print(f"決着！　{self.playerList[self.nowPlay -1]}さんの勝利です！")
            if self.userboard[3][0] == self.marubatu and self.userboard[2][1] == self.marubatu \
            and self.userboard[1][2] == self.marubatu and self.userboard[0][3] == self.marubatu:
                print(f"ビンゴ！ y=xで揃った！")
                print(f"決着！　{self.playerList[self.nowPlay -1]}さんの勝利です！")

                self.bingo = True 
    
    def CheckDrow(self):
        #self.count += 1
        #if self.count == len(self.board)* len(self.board[0]):
        if np.all(self.board != 0):
            print("全てのマスが埋まりました、今回の勝負は引き分けです")
            self.bingo = True
        
        
        


def main():
    test = App()
    test.CreateBoard()
    test.PlayerSet()
    print("ゲームスタート！")
    while test.bingo == False:
        test.Switch()
        test.InputXY()
        test.PlotMark()
        test.ColBingo()
        test.DiagonalBingo()
        test.RowBingo()
        test.CheckDrow()

if __name__ =="__main__":
    main() 