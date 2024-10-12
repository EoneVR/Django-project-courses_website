from .forms import LoginForm, RegisterForm, RequestForm


def auth_forms(request):
    return {
        'login_form': LoginForm(),
        'register_form': RegisterForm()
    }


def request_form_processor(request):
    return {'request_form': RequestForm()}
