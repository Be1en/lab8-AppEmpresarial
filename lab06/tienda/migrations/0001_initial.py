# Generated by Django 4.2.6 on 2023-10-04 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='fecha de registro')),
            ],
        ),
    ]