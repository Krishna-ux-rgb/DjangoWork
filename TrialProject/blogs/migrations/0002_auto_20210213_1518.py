# Generated by Django 3.0.7 on 2021-02-13 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPosts',
            new_name='BlogPost',
        ),
        migrations.RenameModel(
            old_name='Categories',
            new_name='Categorie',
        ),
    ]
