from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext as _
from .pages import listPagesFilter
from .settings import CMS_TEMPLATES, POSEIDON_PAGE_LISTS

class Poseidon(CMSPlugin):
    title = models.CharField(_("Título"), max_length=50)
    pages = models.CharField(_("Páginas a listar"), max_length=50, choices=CMS_TEMPLATES[1:-1])
    type = models.CharField(_("Tipo de lista"), max_length=50, choices=POSEIDON_PAGE_LISTS)
    width = models.IntegerField(_("Largura (px)"), default=640)
    height = models.IntegerField(_("Altura (px)"), default=480)
    count = models.IntegerField(_("Quantidade que será mostrada"), null=True, blank=True)
    needImage = models.BooleanField(_("Precisa ter imagem para aparecer na lista?"))
    max_characters = models.IntegerField(_("Máximo de caracteres do texto"), null=True, blank=True)
    description = models.CharField(_("Subtipo (deixar em branco para não filtrar):"), max_length=50, null=True, blank=True)
    content = models.CharField(_("Conteúdo descritivo"), max_length=500, null=True, blank=True)

    @property
    def highlights(self):
        return listPagesFilter(self.language, self.width, self.height, self.count, self.needImage, self.pages, self.max_characters, self.description)

    def __str__(self):
         return self.title + " (" +  str(len(self.highlights)) + ")"

class Partner(models.Model):
    name = models.CharField(_("Nome"), max_length=50)
    url = models.CharField(_("Link"), max_length=50)
    image = models.ImageField(_("Logo"))

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(_("Nome"), max_length=200)
    email = models.CharField(_("E-mail"), max_length=255)
    phone = models.CharField(_("Telefone"), max_length=20)
    message = models.CharField(_("Mensagem"), max_length=500)

    def __str__(self):
        return self.name + " <" + self.email + "> - "
