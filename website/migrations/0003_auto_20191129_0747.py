# Generated by Django 2.2.7 on 2019-11-29 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20191129_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='content_1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='about',
            name='content_2',
            field=models.TextField(),
        ),
    ]