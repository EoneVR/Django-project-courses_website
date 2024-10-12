from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Courses(models.Model):
    title = models.CharField(max_length=255, verbose_name='Name of course')
    description = models.TextField(default='Description', verbose_name='Description')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Image')
    month = models.IntegerField(default=0, verbose_name='Amount of months')
    price = models.IntegerField(blank=True, null=True, verbose_name='Price per month')
    language = models.TextField(default='Language in which courses are conducted', verbose_name='Languages')
    date_of_start = models.DateTimeField(default=timezone.now, verbose_name='Date of start')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return 'https://www.sarus.uz/public/files/img/news_1528793026.jpg'

    def total_price(self):
        if self.price is None or self.price == 0:
            return 0
        return self.month * self.price

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Comments(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    datetime_create = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='answer')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)

    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            return 'https://icons.veryicon.com/png/o/miscellaneous/rookie-official-icon-gallery/225-default-avatar.png'

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.user.pk})


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"


class Request(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    topic = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.topic}"
