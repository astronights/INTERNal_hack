# Generated by Django 2.2.2 on 2019-06-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20190626_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='company_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='stockprice',
            name='company_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
