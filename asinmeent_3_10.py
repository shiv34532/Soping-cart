d={"january":34,"february":35,"march":36,"april":37,"may":38,"june":39,"july":40,"august":41,"september":47,"october":43,"november":42}
for key, value in d.items():
    if 30 <= value <= 43:
        print("tush month avg temretur avrage betwwen in30 to 43:",key, value)
    else:
        print("this month temretuer is not to both betwwen in 30 to 43 ")