import numpy as np
import pandas as pd

# Pandas数据结构 ---------------------------------
# Series
s = pd.Series([1, 2, 3, np.nan, 5, 6])
print(s)
'''
0   1.0
1   2.0
2   3.0
3   NaN
4   5.0
5   6.0
dtype: float64
'''

# DataFrame
dates = pd.date_range('20200510', periods=6)
# 生成6行4列位置
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
"""
DataFrame.to_excel(excel_writer, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep='inf', verbose=True, 
 freeze_panes=None)
 
excel_writer : 字符串或ExcelWriter 对象，文件路径或现有的ExcelWriter
sheet_name :字符串,默认“Sheet1”，将包含DataFrame的表的名称。
na_rep : 字符串,默认‘ ’，缺失数据表示方式
float_format : 字符串,默认None，格式化浮点数的字符串
columns : 序列,可选，要编写的列
header : 布尔或字符串列表，默认为Ture。写出列名。如果给定字符串列表，则假定它是列名称的别名。
index :布尔,默认的Ture，写行名（索引）
index_label : 字符串或序列，默认为None。如果需要，可以使用索引列的列标签。如果没有给出，标题和索引为true，则使用索引名称。如果数据文件使用多索引，则需使用序列。
startrow :左上角的单元格行来转储数据框
startcol :左上角的单元格列转储数据帧
engine : 字符串,默认没有使用写引擎 - 您也可以通过选项io.excel.xlsx.writer，io.excel.xls.writer和io.excel.xlsm.writer进行设置。
merge_cells : 布尔,默认为Ture编码生成的excel文件。 只有xlwt需要，其他编写者本地支持unicode。
inf_rep : 字符串,默认“正”无穷大的表示(在Excel中不存在无穷大的本地表示)
freeze_panes : 整数的元组(长度2)，默认为None。指定要冻结的基于1的最底部行和最右边的列
"""
df.to_excel('test.xlsx', sheet_name='test', na_rep='缺省值', float_format=None, index=False)
print(df)
'''
                   A         B         C         D
2020-05-10  1.955084  1.217470  0.423107 -0.108163
2020-05-11 -1.057014 -0.063929 -0.029020 -1.096347
2020-05-12 -0.223786 -0.201638 -0.625842 -0.698015
2020-05-13 -1.626282  0.070440 -0.293018  2.079180
2020-05-14  1.170349  0.294723  0.840964 -0.133587
2020-05-15  0.545370 -1.293225  0.161474  0.203340
'''
print(df['B'])
'''
2020-05-10   -1.033668
2020-05-11   -0.999344
2020-05-12   -1.472615
2020-05-13    0.352879
2020-05-14   -0.548522
2020-05-15    0.600731
Freq: D, Name: B, dtype: float64
'''

# 创建特定数据的DataFrame
df_1 = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20200510'),
    'C': pd.Series(2, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(['test', 'train', 'test', 'train']),
    'F': 'foo'
})

print(df_1)
'''
     A          B    C  D      E    F
0  1.0 2020-05-10  2.0  3   test  foo
1  1.0 2020-05-10  2.0  3  train  foo
2  1.0 2020-05-10  2.0  3   test  foo
3  1.0 2020-05-10  2.0  3  train  foo
'''

print(df_1.dtypes)
'''
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
'''

print(df_1.index)
# Int64Index([0, 1, 2, 3], dtype='int64')
print(df_1.columns)
# Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
print(df_1.values)
'''
[[1.0 Timestamp('2020-05-10 00:00:00') 2.0 3 'test' 'foo']
 [1.0 Timestamp('2020-05-10 00:00:00') 2.0 3 'train' 'foo']
 [1.0 Timestamp('2020-05-10 00:00:00') 2.0 3 'test' 'foo']
 [1.0 Timestamp('2020-05-10 00:00:00') 2.0 3 'train' 'foo']]
'''

# 数字总结
print(df_1.describe())
'''
         A    C    D
count  4.0  4.0  4.0
mean   1.0  2.0  3.0
std    0.0  0.0  0.0
min    1.0  2.0  3.0
25%    1.0  2.0  3.0
50%    1.0  2.0  3.0
75%    1.0  2.0  3.0
max    1.0  2.0  3.0
'''

# 翻转数据
print(df_1.T)
'''
                     0                    1                    2  
A                    1                    1                    1   
B  2018-03-10 00:00:00  2018-03-10 00:00:00  2018-03-10 00:00:00   
C                    1                    1                    1   
D                    3                    3                    3   
E                 test                train                 test   
F                  foo                  foo                  foo   

                     3  
A                    1  
B  2018-03-10 00:00:00  
C                    1  
D                    3  
E                train  
F                  foo 
'''

# axis等于1按列进行排序，如ABCDEFG，然后ascending倒序进行显示
print(df_1.sort_index(axis=1, ascending=False))
'''
     F      E  D    C          B    A
0  foo   test  3  2.0 2020-05-10  1.0
1  foo  train  3  2.0 2020-05-10  1.0
2  foo   test  3  2.0 2020-05-10  1.0
3  foo  train  3  2.0 2020-05-10  1.0
'''

# 按值进行排序
print(df_1.sort_values(by='E'))
'''
     A          B    C  D      E    F
0  1.0 2020-05-10  2.0  3   test  foo
2  1.0 2020-05-10  2.0  3   test  foo
1  1.0 2020-05-10  2.0  3  train  foo
3  1.0 2020-05-10  2.0  3  train  foo
'''

# Pandas选择数据 ---------------------------------
dates = pd.date_range('20200510', periods=6)

# 生成6行4列位置
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
'''
                   A         B         C         D
2020-05-10 -2.006642  0.480077  1.184278  0.626612
2020-05-11  1.005898  0.044112  1.148594  0.914532
2020-05-12  1.123702 -0.498627  1.555800 -1.168054
2020-05-13 -0.521166 -0.880080  0.433797  2.076265
2020-05-14 -0.281042  0.254609  0.367603  1.188903
2020-05-15  1.913678 -0.726543 -0.150957  0.437170
'''
# 或者df.A 选择某列
print(df['A'])
'''
2020-05-10    0.706635
2020-05-11   -2.626170
2020-05-12    0.104242
2020-05-13   -0.319969
2020-05-14   -1.214298
2020-05-15   -2.112250
Freq: D, Name: A, dtype: float64
'''

# 切片选择（前闭后开[)）  筛选条件选择
print(df[0:3], '\n', df['20200511': '20200514'])
'''
                   A         B         C         D
2020-05-10 -0.153846  0.340276  0.329010  0.166738
2020-05-11 -0.104547  0.579704  0.892361  0.444797
2020-05-12  1.474382  0.381665 -0.199317 -0.744512 
                    A         B         C         D
2020-05-11 -0.104547  0.579704  0.892361  0.444797
2020-05-12  1.474382  0.381665 -0.199317 -0.744512
2020-05-13  0.608815 -1.480301 -0.406261  1.237358
2020-05-14  1.237255 -0.198100 -0.751383  0.447764
'''

# 根据标签loc-行标签进行选择数据 精确选择
print(df.loc['20200513', ['A', 'B']])
'''
A   -0.793604
B    0.294499
Name: 2020-05-13 00:00:00, dtype: float64
'''

# 根据序列iloc-行号选择数据
print(df.iloc[3, 1])  # 输出第三行第一列的数据
'''
0.9215690192096897
'''

print(df.iloc[3:5, 0:2])  # 切片选择
'''
                   A         B
2020-05-13  2.293163 -0.512940
2020-05-14  0.223289 -1.178493
'''

print(df.iloc[[1, 2, 4], [0, 2]])  # 不连续筛选 iloc([行],[列])
'''
                   A         C
2020-05-11  1.900674  0.279634
2020-05-12  0.172594  0.625444
2020-05-14  2.616086 -0.260998
'''

# print(df.ix[:3, ['A', 'C']])  # pandas的1.0.0版本开始，移除了Series.ix and DataFrame.ix 方法

print(df[df.A > 0])  # 筛选df，A大于0的数据
'''
                   A         B         C         D
2020-05-10  0.076529  0.823211 -0.806683  0.826415
2020-05-11  0.663748 -1.713422  0.168608  0.641277
2020-05-12  0.032350 -0.750164 -0.658109  0.960589
'''

# Pandas设置数据 ---------------------------------
# 根据loc和iloc设置
dates = pd.date_range('20200510', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
'''
             A   B   C   D
2020-05-10   0   1   2   3
2020-05-11   4   5   6   7
2020-05-12   8   9  10  11
2020-05-13  12  13  14  15
2020-05-14  16  17  18  19
2020-05-15  20  21  22  23
'''

df.iloc[2, 2] = 999
df.loc['2020-05-11', 'D'] = 999
print(df)
'''
             A   B    C    D
2020-05-10   0   1    2    3
2020-05-11   4   5    6  999
2020-05-12   8   9  999   11
2020-05-13  12  13   14   15
2020-05-14  16  17   18   19
2020-05-15  20  21   22   23
'''

df[df.A > 18] = 998
print(df)
'''
              A    B    C    D
2020-05-10    0    1    2    3
2020-05-11    4    5    6  999
2020-05-12    8    9  999   11
2020-05-13   12   13   14   15
2020-05-14   16   17   18   19
2020-05-15  998  998  998  998
'''

df['E'] = np.nan
print(df)
'''
              A    B    C    D   E
2020-05-10    0    1    2    3 NaN
2020-05-11    4    5    6  999 NaN
2020-05-12    8    9  999   11 NaN
2020-05-13   12   13   14   15 NaN
2020-05-14   16   17   18   19 NaN
2020-05-15  998  998  998  998 NaN
'''

# Pandas处理丢失数据 ---------------------------------
# 处理数据中NaN数据
dates = pd.date_range('20200510', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df)
'''
             A     B     C   D
2020-05-10   0   NaN   2.0   3
2020-05-11   4   5.0   NaN   7
2020-05-12   8   9.0  10.0  11
2020-05-13  12  13.0  14.0  15
2020-05-14  16  17.0  18.0  19
2020-05-15  20  21.0  22.0  23
'''

# 使用dropna函数去掉NaN的行或列
# 0对行进行操作，1对列进行操作，any只要存在NaN即可drop掉，all必须全部是NaN才可drop
print(df.dropna(axis=0, how='any'))
'''
             A     B     C   D
2020-05-12   8   9.0  10.0  11
2020-05-13  12  13.0  14.0  15
2020-05-14  16  17.0  18.0  19
2020-05-15  20  21.0  22.0  23
'''

# 将NaN替换成0
print(df.fillna(value=0))
'''
             A     B     C   D
2020-05-10   0   0.0   2.0   3
2020-05-11   4   5.0   0.0   7
2020-05-12   8   9.0  10.0  11
2020-05-13  12  13.0  14.0  15
2020-05-14  16  17.0  18.0  19
2020-05-15  20  21.0  22.0  23
'''

# 使用isnull函数判断数据是否丢失
# 矩阵用布尔来进行表示，是nan为true，不是nan为false
print(pd.isnull(df))
'''
                A      B      C      D
2020-05-10  False   True  False  False
2020-05-11  False  False   True  False
2020-05-12  False  False  False  False
2020-05-13  False  False  False  False
2020-05-14  False  False  False  False
2020-05-15  False  False  False  False
'''

# 判断数据中是否存在NaN值
print(np.any(df.isnull()))
'''
True
'''

# Pandas合并数据 ---------------------------------
# axis合并方向
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])
# 0表示竖项合并，1表示横向合并，ingnore_index重置序列index，index变为0 1 2 ...
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res)
'''
     a    b    c    d
0  1.0  1.0  1.0  1.0
1  1.0  1.0  1.0  1.0
2  1.0  1.0  1.0  1.0
3  2.0  2.0  2.0  2.0
4  2.0  2.0  2.0  2.0
5  2.0  2.0  2.0  2.0
6  3.0  3.0  3.0  3.0
7  3.0  3.0  3.0  3.0
8  3.0  3.0  3.0  3.0
'''

# join合并方式
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
# 行往外进行合并
# print(pd.concat([df1, df2], axis=1, join='outer'))
'''
     a    b    c    d    b    c    d    e
1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
4  NaN  NaN  NaN  NaN  1.0  1.0  1.0  1.0
'''
# 行相同的进行合并
# print(pd.concat([df1, df2], axis=1, join='inner'))
'''
     a    b    c    d    b    c    d    e
2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
'''
# 以df1的序列进行合并，df2中没有的序列NaN值填充
print(pd.concat([df1, df2], axis=1).reindex(df1.index))
'''
     a    b    c    d    b    c    d    e
1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
'''

# append添加数据
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# 将df2合并到df1的下面，并重置index
res = df1.append(df2, ignore_index=True)
print(res)
'''
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  1.0  1.0  1.0  1.0
4  1.0  1.0  1.0  1.0
5  1.0  1.0  1.0  1.0
'''

# 将是
# 合并到df1下面，并重置index
res = df1.append(s1, ignore_index=True)
print(res)
'''
     a    b    c    d
0  0.0  0.0  0.0  0.0
1  0.0  0.0  0.0  0.0
2  0.0  0.0  0.0  0.0
3  1.0  2.0  3.0  4.0
'''


# Pandas合并merge ---------------------------------
left = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})
right = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})
res = pd.merge(left, right, on='key')
print(res)
'''
  key   A   B   C   D
0  K0  A0  B0  C0  D0
1  K1  A1  B1  C1  D1
2  K2  A2  B2  C2  D2
3  K3  A3  B3  C3  D3
'''

# 依据两组key合并（key的交集）
left = pd.DataFrame({
    'key1': ['K0', 'K1', 'K2', 'K3'],
    'key2': ['K0', 'K0', 'K1', 'K1'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})
print(left)
'''
  key1 key2   A   B
0   K0   K0  A0  B0
1   K1   K0  A1  B1
2   K2   K1  A2  B2
3   K3   K1  A3  B3
'''
right = pd.DataFrame({
    'key1': ['K2', 'K4', 'K1', 'K5'],
    'key2': ['K1', 'K1', 'K0', 'K0'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})
'''
  key1 key2   C   D
0   K2   K1  C0  D0
1   K4   K1  C1  D1
2   K1   K0  C2  D2
3   K5   K0  C3  D3
'''
print(right)
# 内联合并
res = pd.merge(left, right, on=['key1', 'key2'], how='inner')
print(res)
'''
  key1 key2   A   B   C   D
0   K1   K0  A1  B1  C2  D2
1   K2   K1  A2  B2  C0  D0
'''

# indicator合并
df1 = pd.DataFrame({'col1': [0, 1], 'col_left': ['a', 'b']})
print(df1)
'''
   col1 col_left
0     0        a
1     1        b
'''
df2 = pd.DataFrame({'col1': [1, 2, 2], 'col_right': [2, 2, 2]})
print(df2)
'''
   col1  col_right
0     1          2
1     2          2
2     2          2
'''
# 依据col1进行合并 并启用indicator=True输出每项合并方式（并集）
res = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
print(res)
'''
   col1 col_left  col_right      _merge
0     0        a        NaN   left_only
1     1        b        2.0        both
2     2      NaN        2.0  right_only
3     2      NaN        2.0  right_only
'''

# 依据index合并
left = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
}, index=['K0', 'K1', 'K2'])
print(left)
'''
     A   B
K0  A0  B0
K1  A1  B1
K2  A2  B2
'''

right = pd.DataFrame({
    'C': ['C0', 'C2', 'C3'],
    'D': ['D0', 'D2', 'D3']
}, index=['K0', 'K2', 'K3'])
print(right)
'''
     C   D
K0  C0  D0
K2  C2  D2
K3  C3  D3
'''
# 根据index索引进行合并 并选择外联合并（交集）
res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
print(res)
'''
      A    B    C    D
K0   A0   B0   C0   D0
K1   A1   B1  NaN  NaN
K2   A2   B2   C2   D2
K3  NaN  NaN   C3   D3
'''

res = pd.merge(left, right, left_index=True, right_index=True, how='inner')
print(res)
'''
     A   B   C   D
K0  A0  B0  C0  D0
K2  A2  B2  C2  D2
'''





