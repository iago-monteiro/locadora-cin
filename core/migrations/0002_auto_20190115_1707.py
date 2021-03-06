# Generated by Django 2.1.5 on 2019-01-15 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, verbose_name='Título')),
                ('titulo_original', models.CharField(max_length=150, verbose_name='Título Original')),
                ('sinopse', models.TextField(verbose_name='Sinopse')),
                ('classificacao', models.CharField(choices=[('L', 'Livre'), ('10', 'Não recomendado para menores de 10 anos'), ('12', 'Não recomendado para menores de 12 anos'), ('14', 'Não recomendado para menores de 14 anos'), ('16', 'Não recomendado para menores de 16 anos'), ('18', 'Não recomendado para maiores de 18 anos')], max_length=2, verbose_name='Classificação Indicativa')),
                ('duracao', models.TimeField(verbose_name='Duração')),
                ('diretor', models.CharField(max_length=150, verbose_name='Diretor')),
                ('ano', models.PositiveSmallIntegerField(verbose_name='Ano de Lançamento')),
                ('pais', models.CharField(max_length=150, verbose_name='País')),
            ],
            options={
                'verbose_name': 'Filme',
                'verbose_name_plural': 'Filmes',
                'ordering': ['titulo'],
            },
        ),
        migrations.AlterModelOptions(
            name='genero',
            options={'ordering': ['nome'], 'verbose_name': 'Gênero', 'verbose_name_plural': 'Gêneros'},
        ),
        migrations.AddField(
            model_name='filme',
            name='genero',
            field=models.ManyToManyField(to='core.Genero'),
        ),
    ]
