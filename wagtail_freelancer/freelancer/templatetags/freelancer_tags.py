import re
from django.template.defaultfilters import stringfilter


from django import template
register = template.Library()

@register.simple_tag
@stringfilter
def block_to_list(args):
	re_roles = re.findall(r"dd.[a-zA-Z]*.*dd", args)
	upgraded_list = []
	for role in re_roles:
		new_word = role[3:-4]
		edited_word = new_word.strip('>')
		upgraded_list.append(edited_word)

	return upgraded_list