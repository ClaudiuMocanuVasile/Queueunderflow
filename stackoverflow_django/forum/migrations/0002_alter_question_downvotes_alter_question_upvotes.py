# Generated by Django 4.1.4 on 2023-02-06 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]