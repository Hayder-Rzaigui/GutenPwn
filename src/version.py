#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GutenPwn — version control module.

Versioning scheme: MAJOR.MINOR.PATCH  (semver-inspired)
  MAJOR — breaking changes or major new feature sets
  MINOR — new features, backwards-compatible
  PATCH — bug fixes, small improvements
"""

# Author    : Hayder Rzaigui (@Hayder-Rzaigui)
# GitHub    : https://github.com/Hayder-Rzaigui
# LinkedIn  : https://linkedin.com/in/Hayder-Rzaigui
# X/Twitter : https://x.com/Hayder-Rzaigui

__version__      = "6.3.1"
__version_info__ = (6, 3, 1)
__release_date__ = "2026-06-27"
__author__       = "Hayder Rzaigui"
__license__      = "MIT"


def get_version() -> str:
    """Return the bare version string, e.g. '3.0.0'."""
    return __version__


def get_version_info() -> tuple:
    """Return the version as a (major, minor, patch) tuple."""
    return __version_info__


def get_version_string() -> str:
    """Return formatted version string used in the banner."""
    return f"Version {__version__} ({__release_date__})"
