"""Noxfile for the cookiecutter-robust-python template."""
import nox


nox.options.default_venv_backend = "uv"
nox.options.nox_plugins = [
    "cicd.nox-cookiecutter",
    "cicd.nox-cruft"
]
