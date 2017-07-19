from django.db import models
from django.contrib.auth.models import User
from faker import Factory

# Create your models here.
class Video(models.Model):
    title= models.CharField(blank=True, max_length=100)
    content = models.TextField(blank=True)
    url_image = models.URLField(blank=True)
    editors_choice = models.BooleanField(default=False)
    cover = models.FileField(upload_to='cover_image', null=True)
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    belong_to = models.OneToOneField(to=User, related_name='profile')
    profile_image  = models.FileField(upload_to='profile_image')

    def __str__(self):
        return str(self.belong_to)

class Ticket(models.Model):
    voter = models.ForeignKey(to=UserProfile, related_name='voted_tickets')
    video = models.ForeignKey(to=Video, related_name='tickets')
    VOTE_CHOICE = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
        ('normal', 'Normal'),
    )
    choice = models.CharField(choices=VOTE_CHOICE, max_length=10)

    def __str__(self):
        return str(self.id)
# f = open('C:/Users/Administrator/Desktop/image.txt','r')
# fake = Factory.create()
# for url in f.readlines():
#     v = Video(
#         title = fake.text(max_nb_chars=90),
#         content = fake.text(max_nb_chars=3000),
#         url_image = url,
#         editors_choice = fake.pybool()
#     )
#     v.save()
