# Generated by Django 3.2.6 on 2021-12-16 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taneek', '0006_alter_posts_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_img',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
