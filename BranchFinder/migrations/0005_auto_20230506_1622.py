# Generated by Django 3.2.13 on 2023-05-06 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BranchFinder', '0004_auto_20230506_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passw',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='passw',
            name='updated_at',
        ),
    ]
