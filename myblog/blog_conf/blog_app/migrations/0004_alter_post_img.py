# Generated by Django 4.1.3 on 2022-11-11 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_delete_uploadimage_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
