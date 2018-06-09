from django.core.urlresolvers import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from simplerest.api.urls import urlpatterns
import datetime

"""
La definicion recusriva de fibonacci
fibs(0) = 0
fibs(1) = 1
fibs(n) = fibs(n-1) + fibs(n-2) 
Entonces
fibs(2) = fibs(1) + fibs(0) = 1
fibs(3) = fibs(2) + fibs(1) = 2 ...
Y asi

Voy agregando los elementos obtenidos a f 
"""
def fibs(n):
    f = []
    a = 0
    b = 1
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        f.append(a)
        f.append(b)
        while len(f) != n+1:
            temp = a + b
            f.append(temp)
            a = b
            b = temp

    return f

"""Se cuenta los ( y los  ) si difieren es que no son numeros pares y no estan cerrado"""
def isopen(s):
    return s.count("(") != s.count(")")


@api_view(['GET'])
@permission_classes((AllowAny,))
def home(request):
    """<h2>Este api devuelve la fecha actual usando el formato ISO!</h2>"""
    fecha = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    return Response(
        {"hora_actual": "%s" % fecha})

@api_view(['GET'])
@permission_classes((AllowAny,))
def fibonacci(request):
    """<h3>Fibonacci. /api/fibonacci/?number=5</h3>
        <p>Por defecto es fib(5)</p>
    """
    number = request.GET.getlist('number')
    
    if len(number) > 0:
        ifibonacci = fibs(int(number[0]))
    else:
        ifibonacci = fibs(5)

    return Response({"fibonacci": ifibonacci})

@api_view(['GET'])
def api_list(request):
    """<h3>Log in is required to view this page.</h3>
    """
    apis = []
    for url in urlpatterns:
        apis.append("http://%s%s" % (request.META['HTTP_HOST'], reverse(url._callback_str)))

    return Response({"apis": apis})
