# Generated by Django 2.2.28 on 2024-01-19 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_choice_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='questiontext',
            new_name='question_text',
        ),
    ]
