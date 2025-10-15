from django.urls import path
from . import views
# from django.contrib.sitemaps.views import sitemap
# from .sitemaps import OnCountSitemap  # 先ほど作成したクラス名

# 動的の場合
# sitemaps = {
#     'counts': OnCountSitemap,
# }

# app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]