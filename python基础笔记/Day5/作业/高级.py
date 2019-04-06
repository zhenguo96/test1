# 约瑟夫环问题
# 据说著名犹太历史学家Josephus有过以下的故事：在罗马人占领乔塔帕特后，39 个犹太人与Josephus及他的朋友躲到一个洞中，39个犹太人决定宁愿死也不要被敌人抓到，于是决定了一个自杀方式，41个人排成一个圆圈，由第1个人开始报数，每报数到第3人该人就必须自杀，然后再由下一个重新报数，直到所有人都自杀身亡为止。然而Josephus 和他的朋友并不想遵从。首先从一个人开始，越过k-2个人（因为第一个人已经被越过），并杀掉第k个人。接着，再越过k-1个人，并杀掉第k个人。这个过程沿着圆圈一直进行，直到最终只剩下一个人留下，这个人就可以继续活着。问题是，给定了和，一开始要站在什么地方才能避免被处决？
people = 0
p = []
while 1:
    people += 1
    if people > 41:
        break
    p.append(people)
print(p)
i = 2
while 1:
    if len(p) == 1:
        break
    h = len(p) - 1
    while i <= h:
        p[i] = 0
        i += 3
    print(p)
    if p[-1] == 0:
        i = 2
    elif p[-2] == 0:
        i = 1
    elif p[-3] == 0:
        i = 0
    for j in range(len(p)):
        if 0 in p:
            p.remove(0)
    print(p)
