# Generated by Django 3.2 on 2021-05-15 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adopcion',
            fields=[
                ('numero_adopcion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_adopcion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('nombre', models.CharField(max_length=40)),
                ('raza', models.CharField(max_length=20)),
                ('edad', models.CharField(max_length=20)),
                ('peso', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=30)),
                ('entrenado', models.CharField(choices=[('Entrenado', 'Entrenado(a)'), ('No entrenado', 'No entrenado(a)')], default='Entrenado', max_length=20)),
                ('sexo', models.CharField(choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')], default='Macho', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Persona_adoptiva',
            fields=[
                ('cedula', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(max_length=60)),
                ('primer_apellido', models.CharField(max_length=30)),
                ('segundo_apellido', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='Perros',
        ),
        migrations.AddField(
            model_name='adopcion',
            name='perro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='perros.perro'),
        ),
        migrations.AddField(
            model_name='adopcion',
            name='persona_adoptiva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='perros.persona_adoptiva'),
        ),
    ]