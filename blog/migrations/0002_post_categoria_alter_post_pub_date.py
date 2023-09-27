# Generated by Django 4.2.2 on 2023-09-27 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.CharField(choices=[('noticias', 'Notícias'), ('como_fazer', 'Como Fazer'), ('review', 'Review')], default=None, max_length=15, null=True, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Data Publicação'),
        ),
    ]
