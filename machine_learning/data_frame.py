#数値計算ライブラリインポート
import numpy
#データ分析ライブラリからSeriesとDataFrameをインポート
from pandas import Series, DataFrame

#Series
#data仮引数  : データarray-like, dict, or scalar value
#index仮引数 : データの添え字。array-like or Index (1d)
#dtype仮引数 : データタイプ。numpy.dtype or None
#copy仮引数  : コピー。デフォルトはfalse
#name仮引数  : 結果につける名前
print(Series(data=[0,1]))
print(Series(data=[2,3], index=['x', 'y'], name='value'))

#DataFrame
#data仮引数    : データ ( numpy ndarray (structured or homogeneous), dict, or DataFrame)
#index仮引数   : 要素のインデックス。デフォルトは添え字配列みたいに数字
#columns仮引数 : 2次元のインデックス。デフォルトは数字
#dtype仮引数   : データタイプ。dtype, default None
#copy仮引数    : コピー。デフォルトはfalse。
print(DataFrame(numpy.array([[0,0],[1,1]])))
print(DataFrame(numpy.array([[0,0],[1,1]]), index=['a', 'b']))
print(DataFrame(numpy.array([[0,0],[1,1]]), index=['a', 'b'], columns=['x', 'y']))