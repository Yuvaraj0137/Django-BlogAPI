# Generated by Django 4.1.7 on 2023-03-27 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_blogmodel_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_at',
            field=models.DateField(),
        ),
    ]