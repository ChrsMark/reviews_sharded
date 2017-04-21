from django.db import models
from django.contrib.auth.models import AbstractUser

from django_sharding_library.models import ShardedByMixin
from django_sharding_library.decorators import model_config
from django_sharding_library.fields import TableShardedIDField
from django_sharding_library.models import TableStrategyModel


class User(AbstractUser, ShardedByMixin):
    pass


class ShardedReviewsModelIDs(TableStrategyModel):
    pass


@model_config(shard_group='default', sharded_by_field='user_pk')
class ReviewShardedModel(models.Model):
    id = TableShardedIDField(
        primary_key=True,
        source_table_name=ShardedReviewsModelIDs
    )
    review_string = models.CharField(max_length=120)
    user_pk = models.PositiveIntegerField()

    def get_shard(self):
        from django.contrib.auth import get_user_model
        return get_user_model().objects.get(pk=self.user_pk).shard

    @staticmethod
    def get_shard_from_id(user_pk):
        from django.contrib.auth import get_user_model
        return get_user_model().objects.get(pk=user_pk).shard
