import click
import tomlkit
from ._secrets import get_values
from ._templating import render


@click.command()
@click.option('--template', default=None, help='Template file to use')
@click.option('--target', default=None, help='Target config file')
@click.option('--secret-arn', default=None, help='ARN of the AWS Secrets Manager secret to bind')
@click.option('--config', default='.sprinklesrc', help='sprinkles TOML config file')
def generate_config(template, target, secret_arn, config):
    if template is None:
        with open(config, 'r') as config_file:
            sprinkles_config = tomlkit.loads(config_file.read())
            _secret_arn = secret_arn or sprinkles_config['secret']['arn']
            values = get_values(_secret_arn)
            for section, files in sprinkles_config['files'].items():
                template_path = files['template']
                target_path = files['target']
                click.echo(
                    "Processing [{section}]: {template} -> {target}".format(
                        section=section,
                        template=template_path,
                        target=target_path
                    )
                )
                render(template_path, values, target_path)

    elif secret_arn is not None and template is not None:
        values = get_values(secret_arn)
        render(template, values, target)


if __name__ == '__main__':
    generate_config()
