from django.db import models


class OurTeam(models.Model):
    image = models.ImageField(upload_to='about_ut/our_team')
    name = models.CharField(max_length=400)
    position = models.CharField(max_length=600)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + self.position


class Partner(models.Model):
    image = models.ImageField(upload_to='about_ut/partner')
    name = models.CharField(max_length=400)
    link = models.CharField(max_length=800, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AboutImage(models.Model):
    image = models.ImageField(upload_to='about_ut/main_image')
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=300, default="Male Fashion")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Question(models.Model):
    question = models.CharField(max_length=600)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    our_team = models.ForeignKey(OurTeam, on_delete=models.CASCADE, related_name='message')
    image = models.ImageField(upload_to='about_us/message')
    name = models.CharField(max_length=300, default='Male Fashion')
    message = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class About(models.Model):
    class TitleChoices(models.TextChoices):
        OUR_TEAM = 'Our Team', "OurTeam"
        PARTNER = 'Partner', 'Partner'

    title = models.CharField(choices=TitleChoices.choices)
    title_main = models.CharField(max_length=400, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




