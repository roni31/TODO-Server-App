from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    cretaed = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(auto_now_add=False,auto_now=False,blank=True,null=True)


    def __str__(self):
        return self.title
