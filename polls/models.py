import datetime
from django.db import models
from django.utils import timezone


#  model 추가후 py manage.py makemigrations 명령어로 추가
#  그다음 py manage.py migrate로 추가한다
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        #  등록된 시간=>현재 시간 -어제 이후에시간 이 리스트에 나오도록 설정한 내용
        return self.pub_date > timezone.now() - datetime.timedelta(day=1)

class Choise(models.Model):
    question =models.ForeignKey(Question,on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choise_text

