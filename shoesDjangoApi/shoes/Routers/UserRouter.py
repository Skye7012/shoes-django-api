from rest_framework import routers
from rest_framework.routers import Route, DynamicRoute


class UserRouter(routers.DefaultRouter):
	routes = [
		# List route.
		Route(
			url=r'^{prefix}{trailing_slash}$',
			mapping={
				'get': 'get',
				'put': 'put',
				'delete': 'delete'
			},
			name='{basename}-rud',
			detail=True,
			initkwargs={'suffix': 'Instance'}
		),
		# Dynamically generated list routes. Generated using
		# @action(detail=False) decorator on methods of the viewset.
		DynamicRoute(
			url=r'^{prefix}/{url_path}{trailing_slash}$',
			name='{basename}-{url_name}',
			detail=False,
			initkwargs={}
		),
		# Dynamically generated detail routes. Generated using
		# @action(detail=True) decorator on methods of the viewset.
		DynamicRoute(
			url=r'^{prefix}/{lookup}/{url_path}{trailing_slash}$',
			name='{basename}-{url_name}',
			detail=True,
			initkwargs={}
		),
	]
