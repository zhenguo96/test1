'''
2.企业发放的奖金根据利润提成。
（1）利润低于或等于10万元时，奖金可提10%；
（2）利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
（3）20万到40万之间时，高于20万元的部分，可提成5%；
（4）40万到60万之间时高于40万元的部分，可提成3%；
（5）60万到100万之间时，高于60万元的部分，可提成1.5%，
（6）高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数
'''
profits = float(input("请输入当月利润："))
lirun = [1000000, 600000, 400000, 200000, 100000, 0]
lilv = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
bouns = 0
for i in range(len(lirun)):
    if profits >= lirun[i]:
        bouns += (profits - lirun[i]) * lilv[i]
        profits = lirun[i]
        print(bouns)
print(bouns)












