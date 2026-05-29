import random
import string
import pandas as pd

print('1登入 2註冊 3忘記密碼')

AP = []

while True:
    s = input('選擇服務:')
    if s == '1':
        a = input('帳號:')
        b = input('密碼:')
        found = False
        for u, p in AP:
            if u == a:
                f = True
                if p == b:
                    print('登入成功')
                else:
                    print('密碼錯誤')            
        if not f:
            print('帳號不存在')

    elif s == '2':
        c = input('帳號:')
        f = False
        for u, p in AP:
            if u == c:
                print('帳號已存在')
                f = True
                break
        if not f:
            d = input('密碼:')
            AP.append([c, d])
        
    elif s == '3':
        vc = "".join(random.choices(string.digits, k=6))
        
    elif s == '4':
        print(AP)
        df = pd.DataFrame(AP, columns=['帳號', '密碼'])
        df.to_excel('AP.xlsx', index=False)
    elif s == '5':
        break
    else:
        print('請重新輸入')