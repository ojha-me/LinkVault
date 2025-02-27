from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Bookmarks(models.Model):
    ''' Bookmarks model '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(max_length=500)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=[
        ('Studies', 'Studies'),
        ('Work', 'Work'),
        ('Coding', 'Coding'),
        ('Content Creation', 'Content Creation'),
        ('Other', 'Other'),
    ],
    default= 'Other'
    )
    reminder_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    forgotten_notified = models.BooleanField(default=False)

    def __str__(self):
        return self.title
