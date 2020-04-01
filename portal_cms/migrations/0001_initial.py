# Generated by Django 2.2.17 on 2021-01-07 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poseidon',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='portal_cms_poseidon', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=50)),
                ('pages', models.CharField(choices=[('portal_cms/slides.html', 'Slides'), ('portal_cms/teaching_graduation.html', 'Ensino - Graduação'), ('portal_cms/teaching_post.html', 'Ensino - Pós-graduação'), ('portal_cms/teaching_extension.html', 'Ensino - Extensão'), ('portal_cms/publications_dissertations.html', 'Publicações - Teses'), ('portal_cms/publications_thesis.html', 'Publicações - Dissertações'), ('portal_cms/laboratories.html', 'Laboratórios'), ('portal_cms/research.html', 'Pesquisa e Desenvolvimento'), ('portal_cms/team_member.html', 'Membro do Time')], max_length=50)),
                ('type', models.CharField(choices=[('grid', 'Grade'), ('columns', 'Colunas'), ('horizontal', 'Horizontal'), ('vertical', 'Vertical')], max_length=50)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('count', models.IntegerField()),
                ('needImage', models.BooleanField()),
                ('max_characters', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
