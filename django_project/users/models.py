from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model) :
    user = models.OneToOneField(User,on_delete=models.CASCADE)  # cascade ni bol If User gets deleted , Profile will be also be deleted.
        # One user ni one Profile-toi l gesen ug ym baina.
    image = models.ImageField(default='default.jpeg' , upload_to='profile_pics')
        # profile_pic gesen folder ruu l bugdiign hadgalaad yavaad bainaa gesen ug.
    def __str__(self) :
        return f"{self.user.username} Profile"
    
    def save(self) :
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300 :
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)