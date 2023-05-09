# Generated by Django 3.2.13 on 2023-05-06 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BranchFinder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ApplicationName', models.CharField(max_length=50)),
                ('UserName', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='branch',
            name='BranchCode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='branch',
            name='MICRCODE',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='branch',
            name='PinCode',
            field=models.IntegerField(),
        ),
    ]