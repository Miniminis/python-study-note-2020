# Generated by Django 3.1 on 2020-08-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HelloUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='사용자명')),
                ('userpw', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('regdate', models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')),
            ],
            options={
                'db_table': 'hellousers',
            },
        ),
    ]