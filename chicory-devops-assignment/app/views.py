from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse

CACHE_KEY_NAME = "my_test_key"
CACHE_TTL = 84000

def test_view(request):

	cached = cache.get(CACHE_KEY_NAME)

	if cached:
		cache.incr(CACHE_KEY_NAME, 1)
	else:
		cache.set(CACHE_KEY_NAME, 1, CACHE_TTL)

	return JsonResponse({ "current_value": (cached or 0+1) })