from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #avatar = models.ImageField()
    datecreated = models.DateTimeField('Date created', default=timezone.now())

    homepage = models.URLField('homepage', blank=True, null=True)
    twitterhandle = models.CharField('twitter handle', max_length=30, blank=True, null=True)
    facebookprofile =  models.URLField('facebook profile', blank=True, null=True)
    googleplusprofile = models.URLField('googleplus profile', blank=True, null=True)

    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })
    get_absolute_url = models.permalink(get_absolute_url)

    def __unicode__(self):
        return self.user.get_username()

#def create_user_profile(sender, instance, created, **kwargs):
    #if created:
        #UserProfile.objects.create(user=instance)
#
#post_save.connect(create_user_profile, sender=User)

