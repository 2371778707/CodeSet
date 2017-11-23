# !/usr/bin/env python
#-*-coding:utf-8-*-

import lxml
from lxml import etree
import requests
url = 'http://www.tibet.cn/news/focus/list.shtml'

from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
</div>
'''
html = etree.HTML(text)
# result = etree.tostring(html)
print(type(html))#
from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
</div>
'''
text = requests.get("http://difang.gmw.cn/roll2/2017-11/03/content_120089233.htm").text
html = etree.HTML(text)
result = etree.tostring(html)
print(result)#<class 'lxml.etree._Element'>
a = html.xpath('//div[@id="contentMain"]')#得出的是byte
print(type(a[0]))
print(a[0].encode("utf-8"))
# print(type(html.xpath('//div[@class="each_news"]/h3/a/@href')))#<class 'list'>
# for i in html.xpath('//div[@class="each_news"]/h3/a/@href'):
#     print(i)
#www.30daydo.com/article/222

