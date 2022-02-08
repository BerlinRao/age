driving = input('請你有沒有開過車: ')
if driving != '有' and driving != '沒有':
    print('請輸入有/沒有')
    raise SystemExit
age = input('請輸入年齡: ')
age = int(age)
if driving == '有':
    if age >= 18: 
        print('你通過測驗了')
    else: 
        print('不可以偷開車')
elif driving == '沒有':
    if age >= 18 :
        print('可以考駕照阿')
    else: 
        print('再等一下就可以考了')
