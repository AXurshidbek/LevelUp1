# Generated by Django 4.2.7 on 2023-11-11 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foydalanuvchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('izoh', models.TextField()),
            ],
        ),
    ]
