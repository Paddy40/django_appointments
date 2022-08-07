# Generated by Django 3.2.3 on 2021-05-30 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('descr', models.TextField()),
                ('img', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Doc_table',
        ),
    ]
