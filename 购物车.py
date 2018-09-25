f=open('foods','r',encoding='utf-8')
list=eval(f.read())
user_name=input("请输入用户名")
code=input("请输入密码")
if user_name in list.keys():##读取用户
    if code == list[user_name]['密码']:
        print('欢迎进入')
    else:
        print('密码错误')
        exit()
    print('账户余额',list[user_name]['余额'])
    money=list[user_name]['余额']
else:##添加用户
    list[user_name]={}
    list[user_name]['密码']=code
    list[user_name]['商品']=[]
    money=int(input('请输入收入'))
    list[user_name]['余额']=money
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
]
print(goods)
count=0
while 1:##进入购买环节
    n = int(input('输入商品编号,必须是数字,按9退出,按0输出购买情况'))
    n-=1
    if 0<=n<4:
        spend=goods[n]['price']
        if money>spend:
            money=money-spend
            list[user_name]['商品'].append(goods[n]['name'])
            list[user_name]['余额']=money
            print('\033[32;0m-','商品已加入','-\033[0m')
            print('\033[32;0m-',list[user_name],'-\033[0m')
            print('\033[32;0m-',money,'-\033[0m')
        else:
            print('\033[32;0m\-钱不够-\033[0m ')
    elif n==8:
        print('\033[32;0m-',list[user_name],'-\033[0m')
        print('您的余额','\033[32;0m-',money,'-\033[0m')
        break
    elif n==-1:
        print(list[user_name])
    else:
        print("必须在1-4之间，或9")
f = open('foods', 'w',encoding='utf-8')
f.write(str(list))
f.close()

