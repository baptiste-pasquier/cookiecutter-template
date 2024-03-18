# Cookiecutter Template

[![Build & Test](https://github.com/baptiste-pasquier/cookiecutter-template/actions/workflows/main.yml/badge.svg)](https://github.com/baptiste-pasquier/cookiecutter-template/actions/workflows/main.yml)
[![Code quality](https://github.com/baptiste-pasquier/cookiecutter-template/actions/workflows/quality.yml/badge.svg)](https://github.com/baptiste-pasquier/cookiecutter-template/actions/workflows/quality.yml)
[![Dependencies](https://github.com/baptiste-pasquier/cookiecutter-template/actions/workflows/dependencies.yml/badge.svg)](https://github.com/baptiste-pasquier/cookiecutter-template/actions/workflows/dependencies.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Cookiecutter template for Python projects with Poetry.

**Example project**: https://github.com/baptiste-pasquier/cookiecutter-example

## Features

- Dependency management with [Poetry]
- Pre-commit hooks with [pre-commit]
- Testing with [pytest]
- Code coverage with [Codecov]
- Continuous integration with [GitHub Actions]
- [Ruff] with following plugins:
  - Linting with [Flake8]
  - Code formatting with [Black]
  - Import sorting with [isort]
  - Automated Python syntax upgrades with [pyupgrade]
  - Docstring style checks with [pydocstyle]

[black]: https://github.com/psf/black
[codecov]: https://about.codecov.io/
[flake8]: http://flake8.pycqa.org/en/latest/
[github actions]: https://github.com/features/actions
[isort]: https://pycqa.github.io/isort/
[poetry]: https://python-poetry.org/
[pre-commit]: https://pre-commit.com/
[pydocstyle]: https://www.pydocstyle.org/en/stable/
[pytest]: https://docs.pytest.org/en/latest/
[pyupgrade]: https://github.com/asottile/pyupgrade
[ruff]: https://docs.astral.sh/ruff/

## Usage

1. Install Cookiecutter
```bash
pip install cookiecutter
```

2. Generate a Python project
```bash
cookiecutter https://github.com/baptiste-pasquier/cookiecutter-template
```

## Development

1. Clone the repository
```bash
git clone https://github.com/baptiste-pasquier/cookiecutter-template
```

2. Install the project
- With `poetry` ([installation](https://python-poetry.org/docs/#installation)):
```bash
poetry install
```

3. Install pre-commit
```bash
pre-commit install
```
