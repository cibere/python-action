# python-action

A workflow action to run tools like pyright and ruff on your codebase.

## List of supported tools
- pyright
- ruff (formatter & linter)
- bandit
## Input Reference
### pyright
- **Default**: false
- **Required**: false
- **Type**: bool
- **Description**: whether or not to run pyright. set to "true" to run
### pyright-args
- **Default**: 
- **Required**: false
- **Type**: str
- **Description**: additional args to pass to pyright
### pyright-version
- **Default**: latest
- **Required**: false
- **Type**: str
- **Description**: the version of pyright to use
### ruff-linter
- **Default**: false
- **Required**: false
- **Type**: bool
- **Description**: whether or not to run ruffs linter. set to "true" to run
### ruff-linter-args
- **Default**: 
- **Required**: false
- **Type**: str
- **Description**: additional args to pass to ruffs linter
### ruff-linter-version
- **Default**: latest
- **Required**: false
- **Type**: str
- **Description**: the version of ruff to use when linting
### ruff-formatter
- **Default**: false
- **Required**: false
- **Type**: bool
- **Description**: whether or not to run ruffs formatter. set to "true" to run
### ruff-formatter-args
- **Default**: 
- **Required**: false
- **Type**: str
- **Description**: additional args to pass to ruffs formatter
### ruff-formatter-version
- **Default**: latest
- **Required**: false
- **Type**: str
- **Description**: the version of ruff to use when formatter
### bandit
- **Default**: false
- **Required**: false
- **Type**: bool
- **Description**: whether or not to run bandit. set to "true" to run
### bandit-args
- **Default**: -c pyproject.toml -r .
- **Required**: false
- **Type**: str
- **Description**: args to pass to bandit. Defaults to "-c pyproject.toml -r ."
### bandit-version
- **Default**: latest
- **Required**: false
- **Type**: str
- **Description**: the version of bandit to use
### python-version
- **Default**: 3.13
- **Required**: false
- **Type**: str
- **Description**: the python version to run the tools on
### requirements
- **Default**: 
- **Required**: true
- **Type**: str
- **Description**: "the path to your project's requirements file. if given, requirements will be installed after optionally installing python."
