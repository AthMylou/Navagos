# Generated by Django 5.0.4 on 2024-06-10 08:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='navagos_main.category')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=200)),
                ('question', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='navagos_main.question')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField()),
                ('answer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='navagos_main.answer')),
                ('question', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='navagos_main.question')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_datetime', models.DateTimeField(auto_now_add=True)),
                ('correct_answers', models.IntegerField()),
                ('pass_fail', models.BooleanField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answered_correctly', models.BooleanField()),
                ('chosen_answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='navagos_main.answer')),
                ('question', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='navagos_main.question')),
                ('test', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='navagos_main.test')),
            ],
        ),
    ]
