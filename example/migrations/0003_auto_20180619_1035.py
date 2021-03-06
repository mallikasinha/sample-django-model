# Generated by Django 2.0.6 on 2018-06-19 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_programmer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='programmer',
            name='language',
            field=models.ManyToManyField(to='example.Language'),
        ),
    ]
