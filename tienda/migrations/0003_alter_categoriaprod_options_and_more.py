# Generated by Django 5.0.2 on 2024-04-10 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto_created_producto_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriaprod',
            options={'verbose_name': 'Categoría de Producto', 'verbose_name_plural': 'Categorías de Productos'},
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='categorias',
            new_name='categoria',
        ),
        migrations.AddField(
            model_name='categoriaprod',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoriaprod',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
