from django.db import models



class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name + self.email


class ContactSetting(models.Model):
    title_red = models.CharField(max_length=200)
    title = models.CharField(max_length=400)
    text = models.TextField()
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Address(models.Model):
    title = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    address = models.TextField()

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title