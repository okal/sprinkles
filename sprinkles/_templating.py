from click import echo
from jinja2 import Template


def merge(template_string: str, values: dict):
    template = Template(template_string)
    return template.render(values)


def render(template, values, target=None):
    with open(template, 'r') as template_file:
        template_string = template_file.read()

    output = merge(template_string, values)
    
    if target is not None:
        with open(target, 'w') as target_file:
            target_file.write(output)
    else:
        echo(output)
