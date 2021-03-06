# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from views import chart_resource_image, chart_resource_html_js, chart_resource_json

urlpatterns = patterns('',
    # Provide URL for static image of chart
    url(
        regex = '^projects/p/(?P<project_slug>[-\w]+)/resource/(?P<resource_slug>[-\w]+)/chart/image_png/$',
        view = chart_resource_image,
        name = 'chart_resource_image',),

    # Serve includable JS
    url(
        regex = '^projects/p/(?P<project_slug>[-\w]+)/resource/(?P<resource_slug>[-\w]+)/chart/inc_js/$',
        view = chart_resource_html_js,
        name = 'chart_resource_js',
        kwargs = {"template_name": "resource_chart_js.html"}),

    # Serve HTML code which loads JS data
    url(
        regex = '^projects/p/(?P<project_slug>[-\w]+)/resource/(?P<resource_slug>[-\w]+)/chart/$',
        view = chart_resource_html_js,
        name = 'chart_resource_html',
        kwargs = {"template_name": "resource_chart.html"}),

    # Serve JSON data for table/chart whatever
    url(
        regex = '^projects/p/(?P<project_slug>[-\w]+)/resource/(?P<resource_slug>[-\w]+)/chart/json/$',
        view = chart_resource_json,
        name = 'chart_resource_json',),
)
