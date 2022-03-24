import json
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_csrf_token_view(request, *args, **kwargs):
    if request.method == "GET":
        return HttpResponse()
    return HttpResponseNotAllowed(["GET"])


def add_view(request):
    answer = {}
    if request.body:
        body = json.loads(request.body)
        if body['A'] and body["B"]:
            num1 = float(body['A'])
            num2 = float(body['B'])
            answer['answer'] = (num1 + num2)
            return JsonResponse(answer)
        else:
            answer['error'] = 'Заполните все поля числами'
            return JsonResponse(answer)


def subtract_view(request, *args, **kwargs):
    answer = {}
    if request.body:
        body = json.loads(request.body)
        if body['A'] and body["B"]:
            num1 = float(body['A'])
            num2 = float(body['B'])
            answer['answer'] = (num1 - num2)
            return JsonResponse(answer)
        else:
            answer['error'] = 'Заполните все поля числами'
            return JsonResponse(answer)



def multiply_view(request, *args, **kwargs):
    answer = {}
    if request.body:
        body = json.loads(request.body)
        if body['A'] and body["B"]:
            num1 = float(body['A'])
            num2 = float(body['B'])
            answer['answer'] = (num1 * num2)
            return JsonResponse(answer)
        else:
            answer['error'] = 'Заполните все поля числами'
            return JsonResponse(answer)


def divide_view(request, *args, **kwargs):
    answer = {}
    if request.body:
        body = json.loads(request.body)
        if body['A'] and body["B"]:
            num1 = float(body['A'])
            num2 = float(body['B'])
            answer['answer'] = (num1 / num2)
            return JsonResponse(answer)
        else:
            answer['error'] = 'Заполните все поля числами'
            return JsonResponse(answer)
