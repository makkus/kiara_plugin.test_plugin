# -*- coding: utf-8 -*-

"""Top-level package for kiara_plugin.test_plugin."""

import os

from kiara.utils.class_loading import (
    KiaraEntryPointItem,
    find_data_types_under,
    find_kiara_model_classes_under,
    find_kiara_modules_under,
    find_pipeline_base_path_for_module,
)

__author__ = """Markus Binsteiner"""
__email__ = "markus@frkl.dev"


KIARA_METADATA = {
    "authors": [{"name": __author__, "email": __email__}],
    "description": "Kiara modules for: test_plugin",
    "references": {
        "source_repo": {
            "desc": "The module package git repository.",
            "url": "https://github.com/makkus/kiara_plugin.test_plugin",
        },
        "documentation": {
            "desc": "The url for the module package documentation.",
            "url": "https://makkus.github.io/kiara_plugin.test_plugin/",
        },
    },
    "tags": ["test_plugin"],
    "labels": {"package": "kiara_plugin.test_plugin"},
}
"""Kiara metadata for the `kiara_plugin.test_plugin` module."""


find_modules: KiaraEntryPointItem = (
    find_kiara_modules_under,
    "kiara_plugin.test_plugin.modules",
)
"""Entry point to discover all `kiara` modules for this plugin."""

find_model_classes: KiaraEntryPointItem = (
    find_kiara_model_classes_under,
    "kiara_plugin.test_plugin.models",
)
"""Entry point to discover all `kiara` model classes for this plugin."""

find_data_types: KiaraEntryPointItem = (
    find_data_types_under,
    "kiara_plugin.test_plugin.data_types",
)
"""Entry point to discover all `kiara` data types for this plugin."""
find_pipelines: KiaraEntryPointItem = (
    find_pipeline_base_path_for_module,
    "kiara_plugin.test_plugin.pipelines",
    KIARA_METADATA,
)
"""Entry point to discover all `kiara` pipelines for this plugin."""


def get_version() -> str:
    """Get the current version of the `kiara_plugin.test_plugin` module.

    This tries to get the version from the current git commit or tag, if possible.

    Returns:
        str: The version string.

    """

    from importlib.metadata import PackageNotFoundError, version

    try:
        # Change here if project is renamed and does not equal the package name
        dist_name = __name__
        __version__ = version(dist_name)
    except PackageNotFoundError:
        try:
            version_file = os.path.join(os.path.dirname(__file__), "version.txt")

            if os.path.exists(version_file):
                with open(version_file, encoding="utf-8") as vf:
                    __version__ = vf.read()
            else:
                __version__ = "unknown"

        except Exception:
            pass

        if __version__ is None:
            __version__ = "unknown"

    return __version__
