#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint


# 利用HTMLParser，可以把网页中的文本、图像等解析出来。
class MyHTMLParser(HTMLParser):
    def error(self, message):
        pass

    def __init__(self):
        HTMLParser.__init__(self)
        self.data = []  # 存储html中的数据
        self.links = []

    # 识别html的开始标签
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)
        if tag == 'a':
            if len(attrs) == 0:
                pass
            else:
                for (variable, value) in attrs:
                    if variable == 'href':
                        self.links.append(value)

    # 识别html的结束标签
    def handle_endtag(self, tag):
        print('</%s>' % tag)

    # 识别html的自闭合的标签
    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    # 识别html标签内容
    def handle_data(self, data):
        print(data)

    # 识别html的注释内容
    def handle_comment(self, data):
        print('<!--', data, '-->')

    # 识别html的特殊字符，以&开头的
    def handle_entityref(self, name):
        print('&%s:' % name)

    # 识别html的特殊字符，以&#开头的
    def handle_charref(self, name):
        print('&#%s:' % name)


if __name__ == '__main__':
    html_code = '''<html>
        <head>这是头标签</head>
        <body>
            <!-- test html parser -->
            <a href=\"www.baidu.com\">test</a>
            <p>Some <a href=\"www.qq.com\">html</a> HTML&nbsp;&#1234; Ӓtutorial...<br>END</p>
    </body></html>'''
    parser = MyHTMLParser()
    parser.feed(html_code)
    parser.close()
    print(parser.data)
    print(parser.links)
