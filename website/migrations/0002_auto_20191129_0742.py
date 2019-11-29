# Generated by Django 2.2.7 on 2019-11-29 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='sub_title',
            new_name='sub_title_1',
        ),
        migrations.RemoveField(
            model_name='about',
            name='content',
        ),
        migrations.AddField(
            model_name='about',
            name='content_1',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='content_2',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='sub_title_2',
            field=models.CharField(default='', max_length=127),
            preserve_default=False,
        ),
    ]