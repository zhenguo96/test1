fp = open('2.txt','w')
fp.write('是'.encode('gbk'))
print(fp.read().encode('gbk'))
fp.close()













