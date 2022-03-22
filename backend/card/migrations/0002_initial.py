# Generated by Django 4.0.2 on 2022-03-02 18:15

import auto_prefetch
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("card", "0001_initial"),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="vote",
            name="profile",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="votes", to="user.profile"
            ),
        ),
        migrations.AddField(
            model_name="hashtagtocard",
            name="card",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="card.card"
            ),
        ),
        migrations.AddField(
            model_name="hashtagtocard",
            name="hashtag",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="card.hashtag"
            ),
        ),
        migrations.AddField(
            model_name="hashtagsub",
            name="hashtag",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="card.hashtag"
            ),
        ),
        migrations.AddField(
            model_name="hashtagsub",
            name="profile",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="user.profile"
            ),
        ),
        migrations.AddField(
            model_name="hashtag",
            name="cards",
            field=models.ManyToManyField(
                related_name="hashtags", through="card.HashtagToCard", to="card.Card"
            ),
        ),
        migrations.AddField(
            model_name="hashtag",
            name="subscribers",
            field=models.ManyToManyField(
                related_name="subscriptions", through="card.HashtagSub", to="user.Profile"
            ),
        ),
        migrations.AddField(
            model_name="card",
            name="author",
            field=auto_prefetch.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cards_created",
                to="user.profile",
            ),
        ),
        migrations.AddConstraint(
            model_name="vote",
            constraint=models.UniqueConstraint(
                fields=("profile", "card"), name="user_cant_vote_on_same_card_twice"
            ),
        ),
        migrations.AddConstraint(
            model_name="hashtagtocard",
            constraint=models.UniqueConstraint(
                fields=("hashtag", "card"), name="unique_hashtag_card"
            ),
        ),
        migrations.AddConstraint(
            model_name="hashtagsub",
            constraint=models.UniqueConstraint(
                fields=("hashtag", "profile"), name="unique_hashtag_subscription"
            ),
        ),
    ]
