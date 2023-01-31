from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    #creates instance of user which can be used to delete user and its profile content
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #stores uploaded image using ImageField

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    #To make the userProfile more descriptive we use dunder administrative function of django(it will effect DB value)
    def __str__(self):
        return f'{self.user.username} Profile'



    def save(self,** kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            # if img != ('.RGB'):
            #     img = img.convert('RGB')
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)