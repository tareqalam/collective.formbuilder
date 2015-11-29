# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.formbuilder


class CollectiveFormbuilderLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.formbuilder)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.formbuilder:default')


COLLECTIVE_FORMBUILDER_FIXTURE = CollectiveFormbuilderLayer()


COLLECTIVE_FORMBUILDER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_FORMBUILDER_FIXTURE,),
    name='CollectiveFormbuilderLayer:IntegrationTesting'
)


COLLECTIVE_FORMBUILDER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_FORMBUILDER_FIXTURE,),
    name='CollectiveFormbuilderLayer:FunctionalTesting'
)


COLLECTIVE_FORMBUILDER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_FORMBUILDER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveFormbuilderLayer:AcceptanceTesting'
)
