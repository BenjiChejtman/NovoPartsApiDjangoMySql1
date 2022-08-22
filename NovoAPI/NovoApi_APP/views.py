#from django.shortcuts import render
from django.views import view

class NovoView(View):

    def get(self, request):
        novop = list(company.objects.values())
        if len(novop) > 0:
            datos = {'message': "Success!"}
        else:
            datos = {'message': "Novo Parts not found"}
        return JsonResponse(datos)
    def post(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass