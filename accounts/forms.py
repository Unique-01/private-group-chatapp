from allauth.account.forms import LoginForm
from crispy_forms.helper import FormHelper

class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # self.helper.form_show_labels = False

        self.fields["login"].label = ""
        self.fields["password"].label = ""