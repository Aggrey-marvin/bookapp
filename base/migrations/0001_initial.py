# Generated by Django 4.1.3 on 2022-11-10 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectName', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=256)),
                ('author', models.CharField(max_length=256)),
                ('isbn', models.CharField(max_length=256)),
                ('published', models.DateField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.subject')),
            ],
        ),
    ]