# Generated by Django 3.0.6 on 2020-06-10 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='docuemnt_type',
            field=models.CharField(default='Expense is done by the driver', max_length=256),
        ),
    ]
