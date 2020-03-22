from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import Truncator


class UserProfile(models.Model):
    user          = models.OneToOneField(User, on_delete=models.CASCADE)
    dob           = models.DateField(null=True, blank=True)
    address       = models.TextField(blank=True)
    about_me      = models.TextField(blank=True)
    company       = models.CharField(max_length=50, blank=True)
    occupation    = models.CharField(max_length=50, blank=True)
    email_detail  = models.CharField(max_length=50, blank=True)
    mobile_number = models.CharField(max_length=10, blank=True)
    mobile_detail = models.CharField(max_length=50, blank=True)
    github        = models.CharField(max_length=50, blank=True)
    twitter       = models.CharField(max_length=50, blank=True)
    linkedin      = models.CharField(max_length=50, blank=True)
    facebook      = models.CharField(max_length=50, blank=True)
    instagram     = models.CharField(max_length=50, blank=True)
    thumb_nail    = models.ImageField(upload_to='thumb_nails', blank=True, null=True)

    def __str__(self):
        return self.user.first_name


class UserExperience(models.Model):
    user         = models.ForeignKey(User, related_name='experiences', on_delete=models.CASCADE)
    company      = models.CharField(max_length=50)
    start_date   = models.DateField()
    end_date     = models.DateField()
    job_detail   = models.TextField()
    job_position = models.CharField(max_length=50)
    position     = models.PositiveIntegerField()

    def __str__(self):
        return '{position}: {company}'.format(position=self.job_position, company=self  .company)

    class Meta:
        ordering = ('-start_date',)


class ExperienceWork(models.Model):
    experience  = models.ForeignKey(UserExperience, related_name='experience_works', on_delete=models.CASCADE)
    work_detail = models.CharField(max_length=255)
    position    = models.PositiveIntegerField()

    def __str__(self):
        return Truncator(self.work_detail).chars(25)


class UserEducation(models.Model):
    user       = models.ForeignKey(User,related_name='educations', on_delete=models.CASCADE)
    academy    = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    detail     = models.TextField()
    graduated  = models.DateField()
    position   = models.PositiveIntegerField()

    def __str__(self):
        return self.academy

    class Meta:
        ordering = ('-graduated',)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
