# Generated by Django 5.0.4 on 2024-05-22 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navagos_main', '0002_rename_answers_answer_rename_categories_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='user',
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='value',
            field=models.BooleanField(),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
