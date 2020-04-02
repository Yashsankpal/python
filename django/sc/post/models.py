from django.db import models
from django.urls import reverse
from blog.models import Group
import misaka

from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(User,related_name='post',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    message=models.TextField(blank=True,default='')
    message_html=models.TextField(editable=False,blank=True,default='')
    group=models.ForeignKey(Group,related_name='post', on_delete=models.CASCADE)

    def __str__(self):
        return self.message
        
    def save(self,*args, **kwargs):
        self.message_html=misaka.html(self.message)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("post:single", kwargs={"username":self.user.username,"pk": self.pk})
    
    class Meta:
        ordering=['-created_at']
        unique_together=['user','message']