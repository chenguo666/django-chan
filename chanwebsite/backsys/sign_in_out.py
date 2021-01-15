from django.db import transaction
from django.http import JsonResponse
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.models import User
# 登录 admin1 123456
def signin(request):
    userName=request.POST.get('username')
    passWord=request.POST.get('password')
    print(userName)
    # 使用内置登录
    user=authenticate(username=userName,password=passWord)
    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request,user)
                request.session['usertype']='super'
                return JsonResponse({'result':0, 'msg': '管理员'})
            else:
                login(request, user)
                request.session['usertype'] = 'user'
                return JsonResponse({'result': 0, 'msg': '用户'})
        else:
            return JsonResponse({'result': 0, 'msg': '用户已经被禁用'})
    else:
        return JsonResponse({'result': 1, 'msg': '用户名或者密码错误'})
def signout(requset):
    logout(requset)
    return JsonResponse({'result':0})
# 注册
def reg(request):
    if request.method == 'POST':
        userName = request.POST.get('username')
        passWord = request.POST.get('password')
        email = request.POST.get('email')
        print(userName)
        print(passWord)
        print(email)
        if userName and passWord and email:  # 确保用户名和密码都不为空
            try:
                new_user = User.objects.create_user(username=userName,password=passWord,email=email)
                print(7)
                new_user.is_active = True
                new_user.save
                message = '注册成功'
                return JsonResponse({
                    'ret': 0,
                    'msg': message
                })
            except:
                message = '操作失败请稍后重试！'
                return JsonResponse({
                    'ret': 0,
                    'msg': message
                })
        else:
            message = '请输入用户名密码和邮箱'
            return JsonResponse({
                'ret': 1,
                'msg': message
            })

    else:
        return JsonResponse({'ret':1, 'msg': f'`请使用正确的请求方式'})

# 修改密码：
def updatasign(request):
    userName = request.POST.get('username')
    passWord = request.POST.get('password')
    passWord2 = request.POST.get('password2')
    print(userName)
    user = authenticate(username=userName, password=passWord)
    print(1)
    if user is not None:
        print(2)
        user.set_password(passWord2)
        user.save()
        return JsonResponse({'result': 0, 'msg': '修改成功'})
    else:
        return JsonResponse({'result': 1, 'msg': '无此用户'})