from django.utils.translation import ugettext as _, get_language
from django.shortcuts import render
from cms.models.pluginmodel import CMSPlugin
from .forms import ContactForm
from .models import Contact, Partner
from .pages import listPages, listPagesFilter, getUrl, getTeachingPresentations
from .settings import LANGUAGE_CODE

def home(request):
    lang = get_language()

    if not lang:
        lang = LANGUAGE_CODE
    
    # Main
    slides = listPages(lang, 1920, 480, 5, True, 'slides', 0)

    # Primary
    researchHighlights = listPages(lang, 600, 400, 6, False, 'research', 65)
    researchGrid = {
        'title': _('Pesquisa & Desenvolvimento'),
        'url': getUrl('pesquisa-e-desenvolvimento'),
        'highlights': researchHighlights,
    }

    graduationHighlights = listPagesFilter(lang, 600, 400, 6, False, 'teaching', 65, _('Graduação'))
    postHighlights = listPagesFilter(lang, 600, 400, 6, False, 'teaching', 65, _("Pós-graduação"))
    extensionHighlights = listPagesFilter(lang, 600, 400, 6, False, 'teaching', 65, _("Extensão"))
    
    teachingColumns = {
        'title': _('Ensino'),
        'url': getUrl('ensino'),
        'columns': [
            {
                'title': _('Graduação'),
                'description': getTeachingPresentations(_('Graduação'), _('Descrição Graduação')),
                'url': getUrl('ensino') + "#" + _('Graduação'),
                'highlights':graduationHighlights,
            },{
                'title': _('Pós-graduação'),
                'description': getTeachingPresentations(_('Pós-graduação'), _('Descrição Pós-graduação')),
                'url': getUrl('ensino') + "#" + _('Pós-graduação'),
                'highlights':postHighlights,
            },{
                'title': _('Extensão'),
                'description': getTeachingPresentations(_('Extensão'), _('Descrição Extensão')),
                'url': getUrl('ensino') + "#" + _('Extensão'),
                'highlights':extensionHighlights,
            }
        ]
    }

    laboratoriesHighlights = listPages(lang, 600, 400, 6, False, 'laboratories', 65)
    labsGrid = {
        'title': _("Laboratórios"),
        'highlights': laboratoriesHighlights,
    }

    # Secondary
    articleLinks = listPagesFilter(lang, 600, 400, 10, False, "publications", 65, _("Artigo"))

    thesisLinks = listPagesFilter(lang, 600, 400, 10, False, "publications", 65, _("Dissertação / Tese"))

    return render(request, 'portal_static/home.html', {
        'slides': slides,
        'researchGrid': researchGrid,
        'teachingColumns': teachingColumns,
        'labsGrid': labsGrid,
        'articleLinks': articleLinks,
        'thesisLinks': thesisLinks
    })

def partner(request):
    return render(request, 'portal_static/partners.html', {
        'partners': Partner.objects.all(),
    })

def contact(request):
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            contact = Contact()

            contact.name = form.data['name']
            contact.email = form.data['email']
            contact.phone = form.data['phone']
            contact.message = form.data['message']

            contact.save()

            success = True
    else:
        form = ContactForm()

    return render(request, 'portal_static/contact.html', { 'form': form, 'success': success })
