from django.contrib import admin

from .models import Question,Choise


#  admin내가 등록 db목록을 보기위해서 이와같이 등록한다.
admin.site.register(Question)
admin.site.register(Choise)
