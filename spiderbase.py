# -*- coding: gb2312 -*-
import urllib2,re,os,sys
url_prefix = 'http://www.stats.gov.cn/tjbz/xzqhdm/'
xzqh_url = 't20021125_46784.htm'
print "开始查找"
content = urllib2.urlopen(url_prefix+xzqh_url).read()

code_rule = re.compile(r'<SPAN lang=EN-US style="FONT-SIZE: 12pt; LETTER-SPACING: 0pt">(.*?)</SPAN>')
'''110101&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 东城区'''
codes=re.findall(code_rule,content)
name_rule = re.compile(r'<SPAN style="FONT-SIZE: 12pt; FONT-FAMILY: 宋体; LETTER-SPACING: 0pt; mso-ascii-font-family: \'Times New Roman\'; mso-hansi-font-family: \'Times New Roman\'">(.*?)</SPAN>')        
names=re.findall(name_rule,content)
names.remove('名称')
i=0
string = ''
print len(names)
print len(codes)          
while i < len(names):    
    string=string+codes[i].split('&nbsp')[0]+':'+names[i] + "\n"
    i+=1
print '拼凑结束,写文件'
fileWrite = open('bak.txt','w+')
fileWrite.writelines(string)
fileWrite.close()
print '写文件结束'
        
print "结束"
        
