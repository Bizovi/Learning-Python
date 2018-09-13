from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Classes to manage interaction with DB. Class <> Table
class Post(models.Model):
    """Post table in the DB"""
    title = models.CharField(max_length=150)
    content = models.TextField()
    # auto_now_add can't ever update value of the date
    date = models.DateTimeField(default=timezone.now)
    # deletes a post if you delete the user
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
