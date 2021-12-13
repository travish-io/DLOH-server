from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse


auth_url_bungie = "https://www.bungie.net/en/OAuth/Authorize?client_id=38507&response_type=code"


def home(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"msg": "hello"})


def bungie_login(request: HttpRequest):
    return redirect(auth_url_bungie)


#  api_key = request.query_params.get('api_key', None)
#     if api_key is not None:
#         headers = {
#             'X-API-Key': "85171a1ba12b47c3a02def4c66f45d6f"
#         }
#         return Response(headers)
