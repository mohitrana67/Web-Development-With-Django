from django.db import models
import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_Date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def recently_published(self):
        return self.pub_Date >= timzone.now() - datetime.timedelta(day=1)
        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text