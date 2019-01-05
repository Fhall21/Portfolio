import re

from django import template
register = template.Library()

@register.simple_tag
def block_to_list(args):
	re_roles = re.finall(r"dd.[a-zA-Z]*.*dd", args)
	upgraded_list = []
	for role in re_roles:
		upgraded_list.append(re_roles[role][2:-3])

	return upgraded_list