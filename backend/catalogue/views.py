
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from .models import Catalogue
from .serializers import CatalogueSerializer

# Create your views here.
class CatalogueAPI(APIView):
    renderer_classes = [JSONRenderer]
    @csrf_exempt
    def get(self, request):
        item = Catalogue.objects.all()
        serializer = CatalogueSerializer(item, many=True)
        return Response(serializer.data)