# python-action

A workflow action to run tools like pyright and ruff on your codebase.

## List of supported tools
- pyright
- ruff
- bandit




## Option Reference
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
### python-version
- **Default**: 
- **Required**: false
- **Type**: str
- **Description**: if given, python with the given version will be setup prior to running the tools. if omitted, python will not be setup.
### requirements
- **Default**: 
- **Required**: false
- **Type**: str
- **Description**: "the path to your project's requirements file. if given, requirements will be installed after optionally installing python."
