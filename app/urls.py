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
    path('google51925de0612ccd11/', views.GoogleView.as_view(), name='google'),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]