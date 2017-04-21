# Reviews Sharded
A simple django project for having user's reviews sharded on multiple postgres tables

## About
A simple implementation making use of https://github.com/JBKahn/django-sharding . The goal is to have ReviewShardedModel model sharded on multiple tables according to the user they belong to.

## Make it work
1. clone the repo etc etc
2. Create a virtualenv (optional) to work on
3. pip install -r requirments.txt
4. having already install postgres run: createdb deafult && createdb app_shard_001 && createdb app_shard_002 && createdb app_shard_003 In this way you will have 1 default (unsharded) database and 3 for the sharding. Have a look on the settings.py to understand and add/remove more databases.
5. ./manage.py migrate
6. './manage.py createsuperuser`
7. login to django-admin and create more users.
8. finally you can create ReviewShardedModel objects from your shell

NOTE: `ReviewShardedModel.objects.all() is not expected to work`

For more information the (docs)[http://josephkahn.io/django-sharding/] may come handy.
