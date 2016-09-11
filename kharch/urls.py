from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    url(r'^$', views.index, name='home'),
    url(r'^add-item/$', views.add_item, name='add_item'),
    url(r'^edit-item/$', views.edit_item, name='edit_item'),
    url(r'^delete-item/$', views.delete_item, name='delete_item'),
    url(r'^search-item/$', views.search_item, name='search_item'),
    url(r'^show-items/$', views.show_items, name='show_items'),
    url(r'^history/$', views.history, name='history'),
    url(r'^buy-error/$', views.buy_error, name='buy_error'),
    url(r'^item/(?P<item_name>[-\w]+)/$', views.get_item,name="get_item"),

]