# Generated by Django 3.2.12 on 2022-05-04 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.CharField(max_length=255, verbose_name='Comentário'),
        ),
    ]
