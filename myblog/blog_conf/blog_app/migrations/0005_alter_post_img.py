# Generated by Django 4.1.3 on 2022-11-11 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
