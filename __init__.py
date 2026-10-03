"""Telem plugin for Hermes Agent.

The plugin code ships in the ``telem-sdk`` package, which Hermes installs from
``pyproject.toml`` when the plugin is enabled.
"""

from telem.integrations.hermes import register

__all__ = ["register"]
