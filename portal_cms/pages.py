from cms.models import Page
from easy_thumbnails.files import get_thumbnailer
import re

def listPages(language, width, height, count, needImage, template, max):
    return listPagesFilter(language, width, height, count, needImage, template, max, None)

def listPagesFilter(language, width, height, count, needImage, template, max, subtypeList):
    dbPages = Page.objects.filter(
        publisher_is_draft = False
    )

    if template:
        if not template.startswith('portal_cms'):
            template = 'portal_cms/'+template+'.html'

        dbPages = dbPages.filter(
            template = template
        )
    else:
        dbPages = dbPages.exclude(
            template = 'INHERIT'
        ).exclude(
            template = 'portal_cms/empty.html'
        )

    if dbPages:
        dbPages = dbPages.order_by('-publication_date')[:count]

    pageLinks = []
    
    if subtypeList:
        words = subtypeList.lower().split(',')
        sameSubtype = lambda subtype: list(filter(lambda word: word == subtype, words))

    for dbPage in dbPages:
        imageUrl = getImage(dbPage, width, height)

        if subtypeList:
            subtype = getSubtype(dbPage, language)
            if not subtype or not sameSubtype(subtype.lower()):
                continue

        if imageUrl is None:
            if needImage:
                continue
            else:
                imageUrl='/static/images/portal_default.gif'

        pageLink = {
            'title': cropText(dbPage.get_title(), max),
            'url': dbPage.get_public_url(),
            'description': dbPage.get_meta_description(),
            'date': dbPage.publication_date,
            'draft': dbPage.publisher_is_draft,
            'template': dbPage.template,
            'image': imageUrl,
            'content': getContent(dbPage, language),
        }

        pageLinks.append(pageLink)

    return pageLinks

def getImage(page, width, height):
    placeholders = page.get_placeholders().filter(
        slot='content'
    )

    if not placeholders:
        return None

    content = placeholders[0]

    imagePlugins = content.get_plugins().filter(
        plugin_type='Bootstrap4PicturePlugin'
    )

    if not imagePlugins:
        return None

    # Specific plugin that is being used
    firstPlugin = imagePlugins[0].bootstrap4_picture_bootstrap4picture
    imageUrl = resizeImage(firstPlugin.picture, width, height)

    return imageUrl

def resizeImage(picture, width, height):
    thumbnailer = get_thumbnailer(picture)

    options = {'size': (width, height), 'crop': True, 'upscale': True}
    thumbnail = thumbnailer.get_thumbnail(options)
    return thumbnail.url

def cropText(text, max):
    if not max:
        return text
    if len(text) <= max:
        return text
    resumeTitle = text[0:max]
    if ' ' in resumeTitle:
        while resumeTitle[-1::] != ' ':
            resumeTitle = resumeTitle[0:-1]
        return resumeTitle + '[...]'
    else:
        return resumeTitle + ' [...]'

def getContent(page, language):
    return getPlaceholder(page, language, 'content', 150)

def getSubtype(page, language):
    return getPlaceholder(page, language, 'subtype', 0)

def getPlaceholder(page, language, name, size):
    placeholders = page.get_placeholders().filter(
        slot=name
    )

    if not placeholders:
        return None

    content = placeholders[0]

    textPlugins = content.get_plugins().filter(
        plugin_type='TextPlugin'
    ).filter(
        language=language
    )

    if not textPlugins:
        return None

    firstPlugin = textPlugins[0]

    contentText = firstPlugin.djangocms_text_ckeditor_text.body

    contentText = re.sub(r'<[^>]+>', '', contentText)

    if size:
        contentText = contentText[:size]

    return contentText

def getUrl(pageId):
    pages = Page.objects.filter(reverse_id = pageId) 
    if not pages:
        return ""
    
    return pages[0].get_public_url()

def getTeachingPresentations(subtype, default):
    pages = Page.objects.filter(
        reverse_id = 'ensino'
    ).filter(
        publisher_is_draft = False
    )
    
    for page in pages:
        placeholders = page.get_placeholders()
        
        for placeholder in placeholders:
            plugins = placeholder.get_plugins()
            
            for plugin in plugins:
                instance = plugin.get_plugin_instance()[0]
                if instance and instance.description == subtype.lower():
                    if instance.content:
                        return instance.content

    return default
