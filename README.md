# sprinkles

Sprinkles makes it easy to share configuration files between local dev
environments without leaking private information. No more passwords in Slack
PMs, no more API keys in VCS.

# Usage

Sprinkles reads secrets from AWS secrets manager, and binds them to a template
you provide. The templating is based on Jinja, making it flexible enough to
work with any text-based configuration format you may be using. Anything from
.env files, to Java properties, to yaml.

It has a simple param based CLI API, but can also be executed against a config
file to encourage reuse.

## CLI

1. Output config to stdout

```properties
third.party.api.endpoint=https://example.com/api/v1
third.party.api.key={{THIRD_PARTY_API_KEY}}
```

```
sprinkles --template application.properties.j2 --secret-arn arn:aws:secretsmanager:<region>:<account-id-number>:secret:<secret-name>
```

2. Output to file

```
sprinkles --template application.properties.j2 --secret-arn arn:aws:secretsmanager:<region>:<account-id-number>:secret:<secret-name> --output application.properties
```

## Config file option

Sprinkles also makes it possible to have a set of defaults (tracked in VCS).
Add a .sprinklesrc file in your project root


.sprinklesrc
```toml
[secret-arn]
arn:aws:secretsmanager:<region>:<account-id-number>:secret:<secret-name>

[files]
  [files.docker-env]
    template = sprinkles-templates/.env.sprinkles
    output = .env
  [files.application-properties]
    template = sprinkles-templates/application.properties.sprinkles
    output = src/main/com/example/resources/application-dev.properties
```
