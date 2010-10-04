from django.forms.fields import Field
from django.forms.widgets import Widget

class ModelWidget(Widget):
    """
        Uses a ModelForm to create a widget for a model

        To be used as follows::

            ModelWidget(form=my_model_form)
    """

    def __init__(self):
        super(ModelView, self).__init__()

    def render(self, name, value, attrs=None, choices=()):
        return u'<input type="text" class="autocomplete" autocomplete="off" />'


class ModelField(Field):
    """
        Wrapper around ModelWidget to create compound form fields

        To be used as follows::

            var = ModelField(form=my_model_form)
    """
    pass

