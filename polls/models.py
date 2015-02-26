import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
	    return self.question_text
    def was_published_recently(self):
<<<<<<< HEAD
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
=======
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
>>>>>>> a09eaf31e0dadc3ab34ee4dcab7ae94320b8033c
	was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
	    return self.choice_text
