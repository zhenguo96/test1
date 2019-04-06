# 异常嵌套
try:
    print("zp：周六有空吗，一起去**")
    print("女神：周六要shopping")
    raise ZeroDivisionError("女神：周六要shopping")
except ZeroDivisionError as e:
    try:
        print("zp：正好，一起去")
        print("一起去陈炳德")
        raise ZeroDivisionError("女神：累了")
    except ZeroDivisionError as e:
        print("zp：休息")











