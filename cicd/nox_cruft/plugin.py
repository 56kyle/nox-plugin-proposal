"""Module containing nox plugin logic and hooks."""

import nox


nox.options.sessions = ()


def nox_configure(config: Config) -> None:
    """Nox hook mirroring pytest_configure."""

    # Logic ensuring nox_cookiecutter is registered first despite order they appear in nox_plugins
    if not config.pluginmanager.hasplugin("nox_cookiecutter"):
        config.pluginmanager.register("nox_cookiecutter")


@nox.session(name="generate-demo")
def generate_demo(session: nox.Session) -> None:
    """Generate a demo cookiecutter project."""
    session.install("-e", ".")
    # Logic for generating demo w/ cruft
    # Will cause lint-from-demo from nox-cookiecutter to run using a cruft made demo
