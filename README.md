### Debug mode

Run this at root folder to use debug mode:

```
echo True > DEBUG
```

This creates a file called DEBUG, with "True" written inside.
The settings.py checks this file to activate Debug mode.

The command `python manage.py runserver` runs a server that need
to have DEBUG as True, or else it won't get the static files.

### Generate locale files

Execute these three lines at root folder:

```
django-admin.py makemessages -l pt_BR
rm portal_cms/locale/pt_BR/LC_MESSAGES/django.mo
django-admin.py makemessages -l en_US
rm portal_cms/locale/en_US/LC_MESSAGES/django.mo
python manage.py compilemessages
```

#### Important

Search for `#, fuzzy` with subsequent line starting with `#| msgid ` at .po files.
If there is any occurency, delete the two lines.
If you don't do this, `compilemessages` will ignore the new translations.
