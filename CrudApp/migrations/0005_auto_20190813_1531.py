# Generated by Django 2.0.5 on 2019-08-13 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudApp', '0004_auto_20190813_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(default='SOME STRING', help_text='description', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='facebook',
            field=models.CharField(default='SOME STRING', help_text='facebook link', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.CharField(default='SOME STRING', help_text='password', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(default='SOME STRING', help_text='facebook name', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.CharField(default='SOME STRING', help_text='photo link', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='SOME STRING', help_text='username', max_length=200),
        ),
    ]
