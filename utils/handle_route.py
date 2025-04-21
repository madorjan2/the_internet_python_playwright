def handle_route_wrapper(header: str, value: str):
	def handle_route(route, request):
		headers = request.headers
		headers[header] = value
		route.continue_(headers=headers)

	return handle_route
