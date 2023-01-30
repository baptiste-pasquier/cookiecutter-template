# Cookiecutter Template

[![Build & Test](https://github.com/baptiste-pasquier/cookiecutter-template/actions/workflows/main.yml/badge.svg)](https://github.com/baptiste-pasquier/cookiecutter-template/actions/workflows/main.yml)
[![Code quality](https://github.com/baptiste-pasquier/cookiecutter-template/actions/workflows/quality.yml/badge.svg)](https://github.com/baptiste-pasquier/cookiecutter-template/actions/workflows/quality.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Cookiecutter template for Python projects with Poetry.

**Example project**: https://github.com/baptiste-pasquier/cookiecutter-example

## Features

- Dependency management with [Poetry]
- Linting with [Flake8]
- Code formatting with [Black]
- Import sorting with [isort]
- Automated Python syntax upgrades with [pyupgrade]
- Pre-commit hooks with [pre-commit]
- Testing with [pytest]
- Code coverage with [Codecov]
- Continuous integration with [GitHub Actions]

[black]: https://github.com/psf/black
[codecov]: https://about.codecov.io/
[flake8]: http://flake8.pycqa.org/en/latest/
[github actions]: https://github.com/features/actions
[isort]: https://pycqa.github.io/isort/
[poetry]: https://python-poetry.org/
[pre-commit]: https://pre-commit.com/
[pytest]: https://docs.pytest.org/en/latest/
[pyupgrade]: https://github.com/asottile/pyupgrade

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
