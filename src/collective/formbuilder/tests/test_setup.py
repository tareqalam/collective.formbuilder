# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.formbuilder.testing import COLLECTIVE_FORMBUILDER_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.formbuilder is properly installed."""

    layer = COLLECTIVE_FORMBUILDER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.formbuilder is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.formbuilder'))

    def test_browserlayer(self):
        """Test that ICollectiveFormbuilderLayer is registered."""
        from collective.formbuilder.interfaces import (
            ICollectiveFormbuilderLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveFormbuilderLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_FORMBUILDER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.formbuilder'])

    def test_product_uninstalled(self):
        """Test if collective.formbuilder is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.formbuilder'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveFormbuilderLayer is removed."""
        from collective.formbuilder.interfaces import ICollectiveFormbuilderLayer  # noqa
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveFormbuilderLayer, utils.registered_layers())  # noqa
