# Generated by Django 3.0.5 on 2020-05-02 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='username',
            field=models.CharField(max_length=32, verbose_name='사용자명'),
        ),
    ]