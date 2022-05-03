from django.db import models


class Atracao(models.Model):
    '''
    A classe Atracao serve para armazernar os(as) atrações do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Atracao.
    '''

    nome = models.CharField(
        verbose_name='Nome',
        max_length=100
    )

    descricao = models.TextField(
        verbose_name='Descrição'
    )

    horario_abertura = models.TimeField(
        verbose_name='Horário de abertura'
    )

    horario_fechamento = models.TimeField(
        verbose_name='Horário de fechamento'
    )

    idade_minima = models.PositiveIntegerField(
        verbose_name='Idade mínima'
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'atracoes'
        verbose_name = 'Atração'
        verbose_name_plural = 'Atrações'