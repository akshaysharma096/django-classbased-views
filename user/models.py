from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    profile_pic_url = models.URLField(null=True,blank=True,default='https://cueask.s3.amazonaws.com/avatars_300/male_02.png')
    following = models.ManyToManyField("self", symmetrical = False, related_name = 'followers', blank = True)
    ques_followed = models.ManyToManyField('question.Question', related_name = 'questions_followed', blank = True)
    topic_followed = models.ManyToManyField('topic.Topic', related_name = 'topic_followed', blank = True)
    security_questions = models.ManyToManyField(SecretQuestion, related_name = 'secret_question_user', through = "SecretQuestionAnswer",through_fields=('user','secret_question_1','secret_question_2','secret_question_3'))
    bio=models.CharField(max_length=250,blank=True,null=True)
    class Meta:
        db_table = 'User'  
    
    def __str__(self):
        return self.username