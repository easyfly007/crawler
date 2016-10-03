u = u'中文' #显示指定unicode类型对象u
fout= open('output.txt', 'w')
fout.write("%s" %u.encode('utf-8'))
fout.close()

fin = open('output.txt', 'r')
u = fin.readlines()
for i in u:
	print(str(u))
fin.close()

# str0 = u.encode('gb2312') #以gb2312编码对unicode对像进行编码
# print("str0: ", str0)
# str1 = u.encode('gbk') #以gbk编码对unicode对像进行编码
# print("str1: ", str1)
# str2 = u.encode('utf-8') #以utf-8编码对unicode对像进行编码
# print("str2: ", str2)
# u1 = str0.decode('gb2312')#以gb2312编码对字符串str进行解码，以获取unicode
# print("u1: ", u1)
# u2 = str0.decode('utf-8')#如果以utf-8的编码对str进行解码得到的结果，将无法还原原来的unicode类型
# print(u2)