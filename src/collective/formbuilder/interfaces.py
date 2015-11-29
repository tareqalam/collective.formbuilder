# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from collective.formbuilder import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectiveFormbuilderLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IForm(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )
