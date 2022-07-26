# Generated by Django 3.2.4 on 2022-07-21 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TaskTitle', models.CharField(max_length=30)),
                ('TaskDesc', models.TextField()),
                ('TaskImg', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('Time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
