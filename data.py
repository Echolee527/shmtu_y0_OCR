# -*- coding: UTF-8 -*-
import requests
kv = {'user-agent': 'Mozilla/5.0'}
url = 'https://www.anjuke.com/v3/ajax/captcha/newimage?id=' #这是一个专门的验证码图片网站
for i in range(1, 4): #此处i的范围可以随意修改，用来给图片编号而已
     r=requests.get(url,headers=kv)
     root=r"C:\Users\86155\Pictures\Camera Roll"  #这是图片存储的位置，修改成自己的路径
     path=root+str(i)+'.png'
     with open(path, 'wb') as f:
         f.write(r.content)

