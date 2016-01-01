from plone.dexterity.browser import edit
from plone.dexterity.browser import add
from Products.CMFPlone.resources import add_resource_on_request

resource = 'formbuilder'

class EditForm(edit.DefaultEditForm):

    def update(self):
        add_resource_on_request(self.request, resource)
        super(EditForm, self).update()

class AddForm(add.DefaultAddForm):
    portal_type = 'Form'

    def update(self):
        add_resource_on_request(self.request, resource)
        super(AddForm, self).update()

class AddView(add.DefaultAddView):
    form = AddForm

# EOF
