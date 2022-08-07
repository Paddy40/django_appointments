# Generated by Django 3.2.3 on 2021-06-01 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_appointmenttable_logintable_patienttable'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmenttable',
            name='doctid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='appointmenttable',
            name='patientid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='appointmenttable',
            name='time',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='patienttable',
            name='DoB',
            field=models.DateField(verbose_name='DOB(mm/dd/yyyy)'),
        ),
    ]