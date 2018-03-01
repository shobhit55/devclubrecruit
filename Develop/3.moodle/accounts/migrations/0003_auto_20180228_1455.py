# Generated by Django 2.0.2 on 2018-02-28 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(default='email', max_length=255, unique=True, verbose_name='email address'),
        ),
    ]
