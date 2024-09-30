def bmiCaculator(height, weight):
    bmi = weight / (height/100) ** 2
    if bmi < 18.5:
        state = "體重過輕"
    elif bmi < 24:
        state = "非常標準"
    elif bmi < 27:
        state = "過重"
    elif bmi < 30:
        state = "輕度肥胖"
    elif bmi < 35:
        state = "中度肥胖"
    else:
        state = "過重"

    return bmi,state


while True:
    h = float(input('請輸入您的身高(cm)'))
    w = float(input('請輸入您的體重(kg)'))
    bmi,state = bmiCaculator(height=h,weight=w)
    print("身高是 %.2f公分" % (h))
    print("體重是 %.2f公斤" % (w))
    print("您的bmi是{:d},狀態:{:s}".format(int(bmi),state))
    answer = input("請問還要繼續運算BMI嗎?[繼續請按'Y',停止請按任意鍵]")
    if answer.upper() != 'Y':
        break
    print("-----------------------")
print("程式結束")