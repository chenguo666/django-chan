from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin


class AuthMD(MiddlewareMixin):
    white_list = ['/api/sys/signin','/api/sys/signout','/api/sys/reg','/api/sys/sendemail' ,'/docs','/admin/']  # 白名单
    def process_request(self, request):
        from django.shortcuts import redirect, HttpResponse
        next_url = request.path_info
        # print(request.path_info, request.get_full_path())
        print(next_url)
        if next_url in self.white_list or request.session.get("usertype"):
            print(132456)
            return
        else:
            return JsonResponse({
                    'ret': 5,
                    'msg': "请登录后访问"
                })