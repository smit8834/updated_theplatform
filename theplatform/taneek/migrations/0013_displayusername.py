# Generated by Django 3.2.6 on 2021-12-19 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taneek', '0012_details_phone_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='displayusername',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
