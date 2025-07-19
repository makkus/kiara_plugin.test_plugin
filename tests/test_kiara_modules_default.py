#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `kiara_plugin.test_plugin` package."""

import pytest  # noqa

import kiara_plugin.test_plugin


def test_assert():
    assert kiara_plugin.test_plugin.get_version() is not None
