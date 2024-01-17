from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.serializers.json import DjangoJSONEncoder
from bson import ObjectId


from django.views import View
import json

from .models import JsonData

# Create your views here.
# request handler i.e. action

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Moshi'})

@method_decorator(csrf_exempt, name='dispatch')
class store_json(View):
    def get(self, request, id=None):
        if id:
            try:
                data = JsonData.objects.get(id=id)
                return JsonResponse(data.data, safe=False)
            
            except:
                return JsonResponse({'error': 'data not found'}, status=404)
        else:
            data = JsonData.objects.all()
            all_json = []
            for i in data:
                all_json.append(i.data)
            return JsonResponse(all_json, safe=False)

    def post(self, request):
        try:
            input_data = json.loads(request.body)
            # print(input_data)
            data = JsonData.objects.create(data=input_data)
            return JsonResponse({'id': str(data.id)})
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        
        except KeyError:
            return JsonResponse({'error': 'Missing required fields'}, status=400)