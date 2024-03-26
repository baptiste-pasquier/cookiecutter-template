import shutil
from pathlib import Path

from cookiecutter.main import cookiecutter

# Generate project
cookiecutter(
    template=".",
    no_input=True,
    extra_context={
        "project_name": "Cookiecutter Example",
        "description": "Example of a project generated with cookiecutter-template.",
    },
)

# Remove .git inside
shutil.rmtree(r"cookiecutter-example/.git")

# Edit README
with Path("cookiecutter-example/README.md").open() as f:
    lines = f.readlines()
index = lines.index("Example of a project generated with cookiecutter-template.\n")
lines.insert(
    index + 1,
    "**Template**: https://github.com/baptiste-pasquier/cookiecutter-template\n",
)
lines.insert(index + 1, "\n")
with Path("cookiecutter-example/README.md").open("w") as f:
    f.writelines(lines)
