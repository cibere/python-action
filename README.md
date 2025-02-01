# python-action

A workflow action to run tools like pyright and ruff on your codebase, powered by [uv](https://docs.astral.sh/uv)

## List of supported tools
- pyright
- ruff (formatter & linter)
- bandit

## Input Reference

```yaml
pyright:
  description: 'whether or not to run pyright. set to "true" to run'
  required: false
  default: 'false'
pyright-args:
  description: 'additional args to pass to pyright'
  required: false
  default: ''
pyright-version:
  description: 'the version of pyright to use'
  required: false
  default: 'latest'
ruff-linter:
  description: 'whether or not to run ruffs linter. set to "true" to run'
  required: false
  default: 'false'
ruff-linter-args:
  description: 'additional args to pass to ruffs linter'
  required: false
  default: ''
ruff-linter-version:
  description: 'the version of ruff to use when linting'
  required: false
  default: 'latest'
ruff-formatter:
  description: 'whether or not to run ruffs formatter. set to "true" to run'
  required: false
  default: 'false'
ruff-formatter-args:
  description: 'additional args to pass to ruffs formatter'
  required: false
  default: ''
ruff-formatter-version:
  description: 'the version of ruff to use when formatter'
  required: false
  default: 'latest'
bandit:
  description: 'whether or not to run bandit. set to "true" to run'
  required: false
  default: 'false'
bandit-args:
  description: 'args to pass to bandit. Defaults to "-c pyproject.toml -r ."'
  required: false
  default: '-c pyproject.toml -r .'
bandit-version:
  description: 'the version of bandit to use'
  required: false
  default: 'latest'
python-version:
  description: 'the python version to run the tools on'
  required: false
  default: '3.13'
requirements:
  description: "the path to your project's requirements file. if given, requirements will be installed after optionally installing python."
  required: true
```