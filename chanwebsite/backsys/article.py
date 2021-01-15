import json
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse, HttpResponse
from common.models import Tpyes,article
from django.core.paginator import Paginator,EmptyPage
from django.contrib.auth.models import User

# @login_required
def artlist(request):
    # print(User.objects.all())
    qs = article.objects.values('id', 'title', 'create_date', 'content','type__typename','type_id')
    # logger.info(qs)
    # retlist = list(qs)
    keywords = request.POST.get('keywords', None)
    pagenum = request.POST.get('pagenum')
    pagesize = request.POST.get('pagesize')
    # print(keywords)
    # print(pagenum)
    # print(pagesize)
    if pagesize and pagenum:  # 确保用户名和密码都不为空

    # keywords = request.POST.get('keywords', None)
    # print('************')
    # print(keywords)
        qs=qs.filter(title__contains=keywords)
        # qs=qs.filter(content__contains=keywords)
        # if keywords:
        #     conditions = [Q(title__contaions=one) for one in keywords.split(' ') if one]
        #     query = Q()
        #     for condition in conditions:
        #         query &= condition
        #     qs = qs.filter(query)
        # pagenum = request.POST.get('pagenum')
        # print(pagenum)
        # pagesize = request.POST.get('pagesize')
        # print(pagesize)
        pgnt = Paginator(qs, pagesize)
        page = pgnt.page(pagenum)
        retlist = list(page)
        return JsonResponse({'ret': 0, 'retlist': retlist, 'total': pgnt.count})
        # return JsonResponse({'ret': 0, 'retlist': retlist})
    else:
        return JsonResponse({'ret': 0, 'retlist': '请输入参数'})
# @login_required
def addart(request):
    # print(request.POST.get('sadf'))
    info=request.POST
    # print(info.get('type_id'))
    # if info.get('title') & info.get('content'):
    try:
        with transaction.atomic():
            # create_date = info.get('create_date'),& info.get('create_date')
            new_art = article.objects.create(title=info.get('title'),
                                             content=info.get('content'),type_id=int(info.get('type_id'))
                                             )
        return JsonResponse({'ret': 0, 'id': new_art.id})
    except:
        return JsonResponse({'ret': 0, 'msg':'发生未知错误'})
    # else:
    #     return JsonResponse({'ret': 0, 'msg': '请请填写完整'})
# @login_required
def delart(request):
    infoid = request.POST.get('id')
    try:
        # 根据 id 从数据库中找到相应的客户记录
        artinfo = article.objects.get(id=infoid)
        # print(artinfo)
    except article.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{infoid}`的客户不存在'
        }
    # delete 方法就将该记录从数据库中删除了
    artinfo.delete()
    return JsonResponse({'ret': 0})
# @login_required
def updateart(request):
    info = request.POST
    infoid = request.POST.get('id')
    # print(info)
    try:
        # 根据 id 从数据库中找到相应的客户记录
        artinfo = article.objects.get(id=infoid)
    except article.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{infoid}`的客户不存在'
        }
    artinfo.title = info.get('title')
    artinfo.create_date = info.get('create_date')
    artinfo.content = info.get('content')
    artinfo.type_id = info.get('type_id')
    # 注意，一定要执行save才能将修改信息保存到数据库
    artinfo.save()
    return JsonResponse({'ret': 0})

