# TDD with Python and Django

An attempt reading through "Test-Driven Development with Python" by Harry Percival
with a twist. Instead of using the old Django version, this project tried to use
modern Django version 5.

## Getting Started

This project requires Django version 5 and Python version 3.13.
Create a virtual environment by using `venv` module:

```shell
python -m venv $VIRTUALENV_NAME
# Example: python -m venv .venv
```

Activate the virtual environment:

> Windows

```pwsh
.\.venv\Scripts\Activate.ps1
```

> GNU/Linux (e.g. Ubuntu) and Mac

```shell
source .venv/bin/activate
```

> Notice that your shell prompt will have prefix named after the name of the
> virtual environment.

Install the dependencies, including Django, by using `pip`:

```shell
pip install -r requirements.txt
```

At the end of development, or if you want to exit from the virtual environment,
call `deactivate` command:

```shell
deactivate
```
