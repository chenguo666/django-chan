from django.http import JsonResponse
from common.models import Tpyes
import tushare as ts
from datetime import date, timedelta
ts.set_token('758d91d3dc5618c9e24d7baade463751ee7feeb85a41420086f5a1e9')
pro = ts.pro_api()
def demo(request):
    qs = Tpyes.objects.values()
    retlist = list(qs)
    return JsonResponse({'ret': retlist})

from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
from django.conf import settings
def sendemail(request):
        # 值1：  邮件标题   值2： 邮件主体
        # 值3： 发件人      值4： 收件人
    res = send_mail('关于春节放假通知',
                    '春节放三天假',
                    '1305378470@qq.com',
                    ['1305378470@qq.com'])
    if res == 1:
        return JsonResponse({'result':0})
    else:
        return JsonResponse({'result':1})
# 长篇通讯信息
def chinanews(request):
    yesterday = (date.today() + timedelta(days=-2)).strftime("%Y-%m-%d %H:%M:%S")
    todyday = (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S")
    # print(yesterday)
    # print(todyday)
    try:
        df = pro.major_news(src='',start_date=yesterday, end_date=todyday)
        # df = pro.major_news(src='', start_date='2018-11-21 00:00:00', end_date='2018-11-22 00:00:00')
        info = df.to_dict(orient='records')
        # print(info)
        return JsonResponse({'ret':0,'retlist':info})
    except:
        info="抱歉，您每分钟最多访问该接口2次"
    # print(info)
        return JsonResponse({'ret':1,'retlist':info})
# 新闻联播
def cctv(request):
    # yesterday = (date.today() + timedelta(days=-2)).strftime("%Y-%m-%d %H:%M:%S")
    todyday = (date.today() + timedelta(days=-1)).strftime("%Y%m%d")
    # print(yesterday)
    # print(todyday)
    try:
        df = pro.cctv_news(date=todyday)
    # df = pro.major_news(src='', start_date='2018-11-21 00:00:00', end_date='2018-11-22 00:00:00')
        info = df.to_dict(orient='records')
        return JsonResponse({'ret':0,'retlist':info})
    except:
        info="抱歉，您每分钟最多访问该接口2次"
    # print(info)
        return JsonResponse({'ret':1,'retlist':info})

