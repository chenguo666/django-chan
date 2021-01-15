from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.shortcuts import render
from django.http import JsonResponse
from login.models import User
# Create your views here.

def signin(request):
    if request.method == 'POST':
        userName = request.POST.get('username')
        passWord = request.POST.get('password')
        #
        if userName and passWord:  # 确保用户名和密码都不为空
            userName = userName.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user=User.objects.get(username=userName, password=passWord)
                if user.password == passWord:
                    request.session['usertype'] = 'user'
                    return JsonResponse({'ret': 0})
                else:
                    return JsonResponse({
                    'ret': 1,
                    'msg': f'`{userName}`的用户密码错误'
                })
            except:
                return JsonResponse({
                    'ret': 1,
                    'msg': f'`{userName}`的用户不存在'
                })
    else:
        return JsonResponse({'ret':1, 'msg': f'`请使用正确的请求方式'})


def signout(request):
    return JsonResponse({'ret':2})


def signreg(request):
    if request.method == 'POST':
        userName = request.POST.get('username')
        passWord = request.POST.get('password')
        email = request.POST.get('email')
        sex = request.POST.get('sex')
        print(userName)
        print(passWord)
        print(email)
        print(sex)
        if userName and passWord and email and sex:  # 确保用户名和密码都不为空
            userName = userName.strip()
            email = email.strip()
            print(1)

            if sex=="男" or sex=='女':
                print(2)
                try:
                    same_name_user = User.objects.get(name=userName)
                    print(same_name_user.name)
                    message = '用户已经存在，请重新选择用户名！'
                    return JsonResponse({
                        'ret': 1,
                        'msg': message
                    })
                except:
                    print(3)
                    try:
                        same_email_user = User.objects.get(email=email)
                        print(same_email_user.email)
                        message = '该邮箱地址已被注册，请使用别的邮箱！'
                        return JsonResponse({
                            'ret': 1,
                            'msg': message
                        })
                    except:
                        print(4)
                        try:
                            print(5)
                            with transaction.atomic():
                                print(6)
                                new_user = User.objects.create(name=userName,password=passWord,email=email,sex=sex)
                                new_user.save()
                                message = '注册成功'
                                return JsonResponse({
                                    'ret': 0,
                                    'msg': message
                                })
                        except:
                            message = '操作失败请稍后重试'
                            return JsonResponse({
                                'ret': 1,
                                'msg': message
                            })
            else:
                return JsonResponse({
                    'ret': 1,
                    'msg': f'请选择正确性别'
                })
    else:
        return JsonResponse({'ret':1, 'msg': f'`请使用正确的请求方式'})
    # return JsonResponse({'ret':3})