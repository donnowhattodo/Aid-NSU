# Generated by Django 3.2.9 on 2022-01-07 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20220107_1603'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
