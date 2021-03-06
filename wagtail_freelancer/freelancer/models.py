from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import six
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         StreamFieldPanel)
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, PageBase
from wagtail.images.edit_handlers import ImageChooserPanel

from freelancer.blocks import (
    PortfolioBlock, ProgrammingToolsBlock, TitleRoleBlock, 
    ExtraHeadTagBlock, MissionBlock, TestimonialBlock)
from modelcluster.fields import ParentalKey

from wagtailcaptcha.models import WagtailCaptchaForm

class FreelancerFormField(AbstractFormField):
    page = ParentalKey('FreelancerPage', related_name='form_fields')

#class ProgrammingToolsFormField(AbstractFormField):
#    page = ParentalKey('FreelancerPage', related_name='programming_tools')

class FreelancerPage(WagtailCaptchaForm):
    subtitle = models.CharField(max_length=100, blank=True)

    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    #blocks
    extra_head_tags = StreamField([('extra_head_tags', ExtraHeadTagBlock())], null=True, blank=True)
    title_roles = StreamField([('title_roles', TitleRoleBlock())], null=True, blank=True)
    portfolio = StreamField([('portfolio', PortfolioBlock())], null=True, blank=True)
    mission = StreamField([('mission', MissionBlock())], null=True, blank=True)
    programming_tools = StreamField([('programming_tools', ProgrammingToolsBlock())], null=True, blank=True)
    testimonial = StreamField([('testimonial', TestimonialBlock())], null=True, blank=True)

    about_text = RichTextField(blank=True)
    about_CTA_text = models.CharField(max_length=100, blank=True)
    about_CTA_link = models.URLField(blank=True)

    content_panels = AbstractForm.content_panels + [

        #landing
        StreamFieldPanel('extra_head_tags'),
        MultiFieldPanel([
            FieldPanel('subtitle'),
            ImageChooserPanel('profile_image'),
        ], "Hero"),
        StreamFieldPanel('title_roles'),


        #secondary
        StreamFieldPanel('mission'),
        StreamFieldPanel('portfolio'),
        MultiFieldPanel([
            FieldPanel('about_text', classname="full"),
            FieldPanel('about_CTA_text'),
            FieldPanel('about_CTA_link'),
        ], "Hero"),
        StreamFieldPanel('testimonial'),

        #about
        StreamFieldPanel('programming_tools'),

        #contact
        InlinePanel('form_fields', label="Form fields"),

    ]
'''
To do: add testimonial quotes:
BlockQuoteBlock
wagtail.core.blocks.BlockQuoteBlock

A text field, the contents of which will be wrapped in an HTML <blockquote> tag pair. The keyword arguments required (default: True), max_length, min_length and help_text are accepted.
'''
'''
class ContactPage(WagtailCaptchaEmailForm)
'''