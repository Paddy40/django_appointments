# Generated by Django 3.2.3 on 2021-06-01 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20210530_0814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointmenttable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docname', models.CharField(max_length=100)),
                ('patientname', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Logintable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('psswd', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Patienttable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('DoB', models.DateField()),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Dont want to say')], max_length=1)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('history', models.TextField()),
            ],
        ),
    ]
