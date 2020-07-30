from jinja2 import Template


def merge(template_string: str, values: dict):
    template = Template(template_string)
    return template.render(values)
