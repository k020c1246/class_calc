class MyCalc(object):

  # クラスメンバ変数
  limit = 0

  # コンストラクタ
  def __init__(self):

    # インスタンスメンバ変数
    self.limit=99999

  # インスタンスメソッド
  def SetLimit(self,val):
    self.limit=val

  # クラスメソッド
  #@classmethod
  #def SetLimit(cls,val):
    #cls.limit = val
    
  # クラスメソッド
  @classmethod
  def IsOver(cls,val):
    if val > cls.limit:
      return True
    elif val == cls.limit:
      return True
    else:
      return False
      
  # クラスメソッド
  @classmethod
  def IsUnder(cls ,val):
    if val < cls.limit:
      return True
    elif val == cls.limit:
      return True
    else:
      return False

    # クラスメソッド
  @classmethod
  def IsOver2(cls,val,yes):  #yesは値がlimit(0)と同じ値なら（含む）
    if val > cls.limit:
      yes="含まない"
      print(yes)
      return True
    elif val == cls.limit:
      yes="含む"
      print(yes)
      return True
    else:
      yes="含まない"
      print(yes)
      return False

  
  # クラスメソッド
  @classmethod
  def IsUnder2(cls ,val,yes):
    if val < cls.limit:
      yes="含まない"
      print(yes)
      return True
    elif val == cls.limit:
      yes="含む"
      print(yes)
      return True
    else:
      yes="含まない"
      print(yes)
      return False

# インスタンスを生成して使用できる
mc=MyCalc()
mc.SetLimit(777)
print(mc.limit)

#MyCalc.SetLimit(100)

# インスタンスを生成しなくても使用できる
#print(MyCalc.IsOver2(100,0))
#print(MyCalc.IsOver2(0,0))
#print(MyCalc.IsOver2(-1,0))
#print(MyCalc.IsUnder2(100,0))
#print(MyCalc.IsUnder2(0,0))
#print(MyCalc.IsUnder2(-1,0))