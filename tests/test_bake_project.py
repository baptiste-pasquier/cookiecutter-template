import os
import shlex
import subprocess
from contextlib import contextmanager
from pathlib import Path

import pytest
from cookiecutter.utils import rmtree


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project_path))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    project_path = str(result.project_path)
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, project_slug)
    return project_path, project_slug, project_dir


def _test_common(result):
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()
    assert result.project_path.name == "new-project"

    # Git
    found_toplevel_files = [f.name for f in result.project_path.iterdir()]
    assert ".git" in found_toplevel_files
    gitignore_path = Path(result.project_path, ".gitignore")
    with open(gitignore_path) as f:
        lines = f.readlines()
    assert lines[-1] == "!.gitkeep\n"

    # Poetry
    poetry_lock_path = Path(result.project_path, "poetry.lock")
    with open(poetry_lock_path) as f:
        assert 'name = "flake8"\n' in f.readlines()

    # Pytest
    assert run_inside_dir("pytest", str(result.project_path)) == 0


def _test_data_science(result, use_data_science):
    use_data_science_bool = use_data_science == "yes"

    # Folder
    found_toplevel_files = [f.name for f in result.project_path.iterdir()]
    assert ("data" in found_toplevel_files) is use_data_science_bool

    # Git
    gitignore_path = Path(result.project_path, ".gitignore")
    with open(gitignore_path) as f:
        assert ("data/*\n" in f.readlines()) is use_data_science_bool

    # Poetry
    poetry_lock_path = Path(result.project_path, "poetry.lock")
    with open(poetry_lock_path) as f:
        assert ('name = "scikit-learn"\n' in f.readlines()) is use_data_science_bool


def _test_notebooks(result, use_notebooks):
    use_notebooks_bool = use_notebooks == "yes"

    # Folder
    found_toplevel_files = [f.name for f in result.project_path.iterdir()]
    assert ("notebooks" in found_toplevel_files) is use_notebooks_bool

    # Poetry
    poetry_lock_path = Path(result.project_path, "poetry.lock")
    with open(poetry_lock_path) as f:
        assert ('name = "ipykernel"\n' in f.readlines()) is use_notebooks_bool


def _test_torch(result, use_torch):
    use_torch_bool = use_torch == "yes"

    # Poetry
    poetry_lock_path = Path(result.project_path, "poetry.lock")
    with open(poetry_lock_path) as f:
        assert ('name = "torch"\n' in f.readlines()) is use_torch_bool


@pytest.mark.parametrize("use_data_science", ["no", "yes"])
@pytest.mark.parametrize("use_notebooks", ["no", "yes"])
@pytest.mark.parametrize("use_torch", ["no", "yes"])
def test_bake(cookies, use_data_science, use_notebooks, use_torch):
    with bake_in_temp_dir(
        cookies,
        extra_context={
            "use_data_science": use_data_science,
            "use_notebooks": use_notebooks,
            "use_torch": use_torch,
        },
    ) as result:
        _test_common(result)
        _test_data_science(result, use_data_science)
        _test_notebooks(result, use_notebooks)
        _test_torch(result, use_torch)


def test_pre_commit_up_to_date(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()

        run_inside_dir("pre-commit autoupdate", str(result.project_path))
        run_inside_dir("git add .", str(result.project_path))
        assert (
            run_inside_dir("git diff --cached --exit-code", str(result.project_path))
            == 0
        )
