# Generated by Django 2.1.7 on 2019-03-17 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='shortdesc',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
