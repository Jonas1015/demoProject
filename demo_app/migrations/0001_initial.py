# Generated by Django 2.2.4 on 2019-08-16 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ourData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('', 'Select region'), ('DAR ES SALAAM', 'DAR ES SALAAM'), ('ARUSHA', 'ARUSHA'), ('DODOMA', 'DODOMA'), ('MBEYA', 'MBEYA'), ('KIGOMA', 'KIGOMA'), ('MTWARA', 'MTWARA'), ('TABORA', 'TABORA'), ('MOROGORO', 'MOROGORO'), ('MWANZA', 'MWANZA'), ('KILIMANJARO', 'KILIMANJARO'), ('MARA', 'MARA'), ('IRINGA', 'IRINGA'), ('PWANI', 'PWANI'), ('TANGA', 'TANGA'), ('KAGERA', 'KAGERA'), ('SONGEA', 'SONGEA'), ('SINGIDA', 'SINGIDA'), ('LINDI', 'LINDI'), ('BUKOBA', 'BUKOBA')], max_length=50)),
                ('population', models.PositiveIntegerField()),
                ('number_of_district', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Regional Lists',
            },
        ),
    ]