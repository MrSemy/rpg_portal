from django_filters import FilterSet, DateTimeFilter
from .models import Post


class PostFilter(FilterSet):
    class Meta:
       model = Post
       fields = {
           # поиск по названию
           'title_of_post': ['icontains'],
           'author__user': ['exact'],
           'date_of_post': ['gt'],
           'category': ['exact']
        }
       filter_overrides = {
           DateTimeFilter: {
               'filter_class': DateTimeFilter,
               'extra': lambda f: {
                   'widget': DateTimeFilter,
               },
           },
       }