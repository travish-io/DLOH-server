from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse


auth_url_bungie = "https://www.bungie.net/en/OAuth/Authorize?client_id=38507&response_type=code"


def home(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"msg": "hello"})


def bungie_login(request: HttpRequest):
    return redirect(auth_url_bungie)
