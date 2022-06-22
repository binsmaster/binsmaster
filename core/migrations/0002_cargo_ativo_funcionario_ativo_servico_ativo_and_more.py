# Generated by Django 4.0.5 on 2022-06-14 13:46

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
        migrations.AddField(
            model_name='servico',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='criados',
            field=models.DateField(auto_now_add=True, verbose_name='Criação'),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='modificado',
            field=models.DateField(auto_now=True, verbose_name='Atualização'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='criados',
            field=models.DateField(auto_now_add=True, verbose_name='Criação'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='modificado',
            field=models.DateField(auto_now=True, verbose_name='Atualização'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='criados',
            field=models.DateField(auto_now_add=True, verbose_name='Criação'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='modificado',
            field=models.DateField(auto_now=True, verbose_name='Atualização'),
        ),
    ]