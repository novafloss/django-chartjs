from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from . import views

home = TemplateView.as_view(template_name='home.html')

urlpatterns = patterns(
    '',
    url(r'^$', home, name='home'),
    url(r'^colors/$', views.colors, name='colors'),

    # Column
    url(r'^column_highchart/json/$', views.column_highchart_json,
        name='column_highchart_json'),

    # Line chart
    url(r'^line_chart/$', views.line_chart,
        name='line_chart'),
    url(r'^line_chart/json/$', views.line_chart_json,
        name='line_chart_json'),
    url(r'^line_highchart/json/$', views.line_highchart_json,
        name='line_highchart_json'),

    # Pie
    url(r'^pie_highchart/json/$', views.pie_highchart_json,
        name='pie_highchart_json'),
    url(r'^donut_highchart/json/$', views.donut_highchart_json,
        name='donut_highchart_json'),
)
