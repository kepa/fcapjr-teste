# -*- coding: utf-8 -*-
from django.db import models
# Banner (img,descricao)
# Area de membros (nome da area e membros)
# membro (nome, cargo)

class Banner(models.Model):

    image = models.ImageField(
        verbose_name='Imagem', upload_to='images',
        blank=True, null=True
    )

    title = models.TextField('Titulo', max_length=25, blank=True, null=True)

    description = models.TextField('Descricao', max_length=255,
                                 blank=True, null=True)

    def __unicode__(self):
        return unicode(self.title) or u''


class Area(models.Model):

    nome = models.CharField('nome da area', max_length=255)

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"

    def __unicode__(self):
        return unicode(self.nome) or u''


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
        return unicode(self.nome) or u''

################## Description, Missao, visao, valores ##################
class Description(models.Model):
    text = models.TextField(verbose_name='QuemSomos');

    def __unicode__(self):
        return "Quem Somos"

class Mission(models.Model):

    image = models.ImageField(
        verbose_name='Imagem', upload_to='images',
        blank=True, null=True
    )
    title = models.CharField(
        'Titulo', max_length=255, blank=True, null=True)

    description = models.TextField(
        'Missao', max_length=255, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.title) or u''


class Vision(models.Model):

    image = models.ImageField(
        verbose_name='Imagem', upload_to='images',
        blank=True, null=True
    )
    title = models.CharField(
        'Titulo', max_length=255, blank=True, null=True)

    description = models.TextField(
        'Visao', max_length=255, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.title) or u''


class ValueDescription(models.Model):
    # associatedImage = models.ManyToManyField(Value)
    description = models.TextField(
        'Descricao', max_length=255, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.description) or u''


class Value(models.Model):

    image = models.ImageField(
        verbose_name='Imagem', upload_to='images',
        blank=True, null=True
    )

    title = models.CharField(
        'Titulo', max_length=255, blank=True, null=True)

    valuesDescription = models.ManyToManyField(ValueDescription)

    def __unicode__(self):
        return unicode(self.title) or u''