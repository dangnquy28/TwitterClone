from django.db import models

from cloudinary.models import CloudinaryField


# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table= 'post'

    name= models.CharField(
        'Name', blank= False, null= False, max_length=140, db_index=True, default='Anonymous'
    )

    body= models.CharField(
        'Body', blank= False, null= False, max_length= 140,db_index= True
    )
    image = CloudinaryField('image', blank= True)

    created_at= models.DateTimeField(
        'Created Datetime', blank= True, auto_now=True
    )
    likes= models.PositiveIntegerField('like count', default=0, null=True, blank=True)

    def __str__(self):
        return self.name
    
    



