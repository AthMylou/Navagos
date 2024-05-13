# Generated by Django 5.0.4 on 2024-04-26 10:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_datetime', models.DateTimeField(auto_now=True)),
                ('correct_answers', models.IntegerField()),
                ('pass_fail', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('passwd', models.CharField(max_length=100)),
                ('age', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='navagos_main.categories')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BinaryField()),
                ('answer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='navagos_main.answers')),
                ('question', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='navagos_main.questions')),
            ],
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='navagos_main.questions'),
        ),
        migrations.CreateModel(
            name='TestQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answered_correctly', models.BooleanField()),
                ('question', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='navagos_main.questions')),
                ('test', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='navagos_main.tests')),
            ],
        ),
        migrations.AddField(
            model_name='tests',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='navagos_main.users'),
        ),
    ]