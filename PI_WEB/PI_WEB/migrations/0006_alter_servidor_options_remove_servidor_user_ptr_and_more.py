# Generated by Django 4.2.2 on 2023-07-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PI_WEB', '0005_alter_servidor_options_remove_servidor_last_login_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servidor',
            options={},
        ),
        migrations.RemoveField(
            model_name='servidor',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='servidor',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='servidor',
            name='password',
            field=models.CharField(default='', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]