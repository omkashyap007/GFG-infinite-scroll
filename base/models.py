from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    title = models.CharField(max_length = 200 , blank = False , null = False)
    content = models.CharField(max_length = 200 , blank = False , null = False)


    def __str__(self):
        return f"{self.user.username} wrote {self.title[:50]} "

    