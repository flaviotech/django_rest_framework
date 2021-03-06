from core.models import PontoTuristico
from django.http import HttpResponse
from rest_framework import filters, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import (DjangoModelPermissions, IsAdminUser,
                                        IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from ..serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    permission_classes = [
        DjangoModelPermissions,
    ]

    authentication_classes = [
        TokenAuthentication,
    ]
    
    filter_backends = [
        filters.SearchFilter,
    ]

    search_fields = [
        'nome',
        'descricao',
    ]

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = queryset.filter(id=id)

        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        
        if descricao:
            queryset = queryset.filter(descricao__icontains=descricao)
        
        return queryset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, pk):
        atracoes = request.data['ids']
        ponto_turistico = PontoTuristico.objects.get(pk=pk)
        ponto_turistico.atracoes.set(atracoes)

        ponto_turistico.save()
        return HttpResponse('OK')
