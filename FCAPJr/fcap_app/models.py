# -*- coding: utf-8 -*-
from django.db import models
# Banner (img,descricao)
# Area de membros (nome da area e membros)
# membro (nome, cargo)


class Banner(models.Model):

    imagem = models.ImageField('Imagem')
    descricao = models.TextField('Descricao', max_length=255,
                                 blank=True, null=True)

    def __unicode__(self):
        pass


class Area(models.Model):

    nome = models.CharField('nome da area', max_length=255)

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"

    def __unicode__(self):
        pass


class Membro(models.Model):

    area = models.ForeignKey(Area)

    nome = models.CharField('nome', max_length=255,
                            blank=False, null=False)
    Cargo = models.CharField('cargo', max_length=255,
                             blank=True, null=True)

    class Meta:
        verbose_name = "Membro"
        verbose_name_plural = "Membros"

    def __unicode__(self):
        pass

