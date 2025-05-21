from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model) :

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)  # end paranthysis baihgui bga ni we don't wanna e xecute this function. We need to only pass it as an argument.
    author = models.ForeignKey(User , on_delete=models.CASCADE)
        # many-to-one relationship--iig ashiglah uyd iim Foreign blah2
    """Foreign key asiglaad shaachihaar , shuud neg User ni many Post-toi bj bolohba , post ni 1 l authorti bian."""
    def __str__(self) :
        return self.title

    def get_absolute_url(self) :
        return reverse('post-detail',kwargs={'pk':self.pk})  # primary_key gesen ug ym baina :: pk.
    
    