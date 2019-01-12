from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel)
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock



class PortfolioBlock(blocks.StructBlock):
    heading = blocks.CharBlock(classname="full title")
    image = ImageChooserBlock()
    intro = blocks.RichTextBlock()

    class Meta:
        template = 'freelancer/blocks/portfolio.html'

class ProgrammingToolsBlock(blocks.StructBlock):
    logo = ImageChooserBlock()

    class Meta:
        template = 'freelancer/blocks/programming_tools.html'
class TitleRoleBlock(blocks.StructBlock):
    role = blocks.CharBlock()


class ExtraHeadTagBlock(blocks.StructBlock):
    tag = blocks.RawHTMLBlock()

    class Meta:
        template = 'freelancer/blocks/extra_tags.html'

class MissionBlock(blocks.StructBlock):
    text = blocks.CharBlock()

    icon_link = blocks.RawHTMLBlock(required=False)
    img_required = blocks.BooleanBlock(required=False)
    icon_img = ImageChooserBlock(required=False)

    class Meta:
        template = 'freelancer/blocks/mission.html'

class TestimonialBlock(blocks.StructBlock):
    testimonial = blocks.BlockQuoteBlock()
    author = blocks.CharBlock()

    class Meta:
        template = 'freelancer/blocks/testimonials.html'