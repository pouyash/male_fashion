# Generated by Django 4.2.1 on 2023-05-29 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_setting', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='about_ut/our_team')),
                ('name', models.CharField(max_length=400)),
                ('position', models.CharField(max_length=600)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_setting', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='about_ut/partner')),
                ('name', models.CharField(max_length=400)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]