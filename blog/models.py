from django.db import models

class Blog(models.Model):
    subject = models.CharField(verbose_name='件名',max_length=50,)
    content = models.TextField(verbose_name='本文',max_length=250,)
    postdate = models.DateTimeField(auto_now_add=True)
