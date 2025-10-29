"""Module containing nox plugin logic and hooks."""

import nox


@nox.session(name="generate-demo")
def generate_demo(session: nox.Session) -> None:
    """Generate a demo cookiecutter project."""
    session.install("-e", ".")
    # Logic for generating demo w/ cookiecutter


@nox.session(name="lint-from-demo")
def lint_from_demo(session: nox.Session) -> None:
    """Generate a demo, lint it, then use retrocookie to propagate those changes to the cookiecutter itself."""
    session.install("-e", ".")
    # Logic for generating a demo, linting, then running retrocookie
