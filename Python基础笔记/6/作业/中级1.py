# 1.现有商品列表如下：
# products = [['Iphone8', 6666], ['MacPro', 8888], ['小米 ', 9999], ['Coffee', 9999], ['Book', 9888]]
# 请编程打印出这样的格式：
# --------商品列表--------
# 0.Iphone8 6666
# 1.MacPro 8888
# 2.小米  9999
# 3.Coffee 9999
# 4.Book 9888
products = [['Iphone8', 6666], ['MacPro', 8888], ['小米 ', 9999], ['Coffee', 9999], ['Book', 9888]]
for i in range(len(products)):
    print(i,products[i][0] , products[i][1])

