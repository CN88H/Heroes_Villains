from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializers
from .models import Super


@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        types = request.query_params.get('super_type')
        print(types)

        supers = Super.objects.all()

        if types:
            supers = supers.filter(super_type__type=types)

        serializer = SuperSerializers(supers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)  
    if request.method == 'GET':
        serializer = SuperSerializers(super)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SuperSerializers(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELECT':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

