# Generated by Django 3.2.6 on 2021-12-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taneek', '0014_auto_20211219_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
