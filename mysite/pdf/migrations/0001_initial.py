# Generated by Django 4.1.1 on 2023-01-12 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.IntegerField(max_length=200)),
                ('summary', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('school', models.CharField(max_length=200)),
                ('university', models.CharField(max_length=200)),
                ('previous_work', models.TextField(max_length=1000)),
                ('skills', models.TextField(max_length=1000)),
            ],
        ),
    ]
