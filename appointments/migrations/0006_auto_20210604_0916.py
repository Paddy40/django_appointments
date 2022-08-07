# Generated by Django 3.2.3 on 2021-06-04 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_querytable'),
    ]

    operations = [
        migrations.AddField(
            model_name='logintable',
            name='givenid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='logintable',
            name='name',
            field=models.CharField(default='abc', max_length=100),
        ),
        migrations.AlterField(
            model_name='logintable',
            name='uname',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
