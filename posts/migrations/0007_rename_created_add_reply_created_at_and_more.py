# Generated by Django 4.2 on 2023-05-13 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_rename_created_add_tweet_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='created_add',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='updated_ad',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='replyreaction',
            name='reply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_reactions', to='posts.reply'),
        ),
    ]
