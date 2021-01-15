from django.urls import path
from backsys import sign_in_out,article,arthors

urlpatterns=[
    path('signin', sign_in_out.signin),
    path('signout', sign_in_out.signout),
    path('reg', sign_in_out.reg),
    path('updatasign', sign_in_out.updatasign),
    path('artlist', article.artlist),
    path('addart', article.addart),
    path('delart', article.delart),
    path('updateart', article.updateart),
    path('demo',arthors.demo),
    path('sendemail',arthors.sendemail),
    path('chinanews',arthors.chinanews),
    path('cctv',arthors.cctv),
]