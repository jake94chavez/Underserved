from django.contrib import admin


# Register your models here.

from.models import Filter
from.models import Game
from.models import Index

# Register your models here.
admin.site.register(Filter)
admin.site.register(Game)
admin.site.register(Index)
