# Generated by Django 3.2 on 2023-03-29 07:40

from django.db import migrations, models
import django.db.models.deletion
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_userprofile_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('sku', models.CharField(db_index=True, max_length=20, validators=[utils.validators.SKUValidator()], verbose_name='stock keeping unit')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('avatar', models.ImageField(blank=True, upload_to='package/', verbose_name='avatar')),
                ('is_enable', models.BooleanField(default=True, verbose_name='is enable')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('duration', models.DurationField(blank=True, null=True, verbose_name='duration')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated time')),
            ],
            options={
                'verbose_name': 'Package',
                'verbose_name_plural': 'Packages',
                'db_table': 'package',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('expire_time', models.DateTimeField(blank=True, null=True, verbose_name='expire time')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='subscriptions.package')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='users.user')),
            ],
            options={
                'verbose_name': 'Subscription',
                'verbose_name_plural': 'Subscriptions',
                'db_table': 'subscriptions',
            },
        ),
    ]
