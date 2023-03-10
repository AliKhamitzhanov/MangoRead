# Generated by Django 4.1.4 on 2023-01-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=80, unique=True)),
                ('nickname', models.CharField(max_length=45)),
                ('photo', models.ImageField(upload_to='media/user_photo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
