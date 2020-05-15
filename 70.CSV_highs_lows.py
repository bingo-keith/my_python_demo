import csv
from datetime import datetime

from matplotlib import pyplot as plt

# 从文件中获取最高气温
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    dates, highs = [], []
    for row in reader:
        highs = row[1:]
        print(row[0])
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')
# plt.plot(dates, highs, c='red')  # x轴日期标签，因源文件格式问题，运行报错

# 设置图形的格式
plt.title('Daily high temperatures, July 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

"""
    datetime.strptime(date, '%Y-%m-%d') 
    %A 星期的名称，如 Monday
    %B 月份名，如 January
    %m 用数字表示的月份（ 01~12 ）
    %d 用数字表示月份中的一天（ 01~31 ）
    %Y 四位的年份，如 2015
    %y 两位的年份，如 15
    %H 24 小时制的小时数（ 00~23 ）
    %I 12 小时制的小时数（ 01~12 ）
    %p am 或 pm
    %M 分钟数（ 00~59 ）
    %S 秒数（ 00~61 ）
"""
