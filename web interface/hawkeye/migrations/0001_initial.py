# Generated by Django 3.0 on 2020-12-28 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(help_text='img name', max_length=20)),
                ('imgquery', models.ImageField(upload_to='')),
            ],
        ),
    ]
