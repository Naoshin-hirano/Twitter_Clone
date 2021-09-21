from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=280)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_id