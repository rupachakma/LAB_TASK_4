# Generated by Django 4.2.6 on 2023-10-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40)),
                ('mobile_number', models.IntegerField()),
                ('profilepic', models.ImageField(blank=True, null=True, upload_to='img')),
            ],
        ),
    ]
