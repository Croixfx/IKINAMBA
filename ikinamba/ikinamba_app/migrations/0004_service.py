# Generated by Django 5.1.4 on 2024-12-15 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ikinamba_app', '0003_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]