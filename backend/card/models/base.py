from django.db import models

TILE_LENGTH = 200


class CardBase(models.Model):
    TILE_FIELDS = [f"tile_{n}" for n in range(1, 26)]
    TILE_LENGTH = TILE_LENGTH
    TITLE_LENGTH = 50

    title = models.CharField(max_length=TILE_LENGTH)
    created_at = models.DateTimeField(auto_now_add=True)
    created_timestamp = models.FloatField(default=0)

    edited_at = models.DateTimeField(auto_now=True)
    edited_timestamp = models.FloatField(default=0)

    up = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

    @staticmethod
    def tile_field():
        return models.CharField(max_length=TILE_LENGTH)

    tile_1 = tile_field()
    tile_2 = tile_field()
    tile_3 = tile_field()
    tile_4 = tile_field()
    tile_5 = tile_field()
    tile_6 = tile_field()
    tile_7 = tile_field()
    tile_8 = tile_field()
    tile_9 = tile_field()
    tile_10 = tile_field()
    tile_11 = tile_field()
    tile_12 = tile_field()
    tile_13 = tile_field()
    tile_14 = tile_field()
    tile_15 = tile_field()
    tile_16 = tile_field()
    tile_17 = tile_field()
    tile_18 = tile_field()
    tile_19 = tile_field()
    tile_20 = tile_field()
    tile_21 = tile_field()
    tile_22 = tile_field()
    tile_23 = tile_field()
    tile_24 = tile_field()
    tile_25 = tile_field()

    class Meta:
        abstract = True

    def __str__(self):
        return " ".join(
            (
                f"({self.id})",
                f'"{self.title}"',
            )
        )


class VoteBase(models.Model):
    created_at = models.DateTimeField(auto_now=True)

    up_state = models.IntegerField(default=0)
    down_state = models.IntegerField(default=0)
    up = models.IntegerField()

    class Meta:
        abstract = True


class HashtagBase(models.Model):
    NAME_LENGTH = CardBase.TITLE_LENGTH - 1

    name = models.CharField(
        max_length=NAME_LENGTH,
        unique=True,
        primary_key=True,
    )

    class Meta:
        abstract = True


class HashtagProfileBase(models.Model):
    is_subscribed = models.IntegerField(default=1)

    class Meta:
        abstract = True
