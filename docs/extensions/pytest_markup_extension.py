from enum import Enum

class ToastStatus(Enum):
    Skipped = "skipped"
    Parametrize = "parametrize"

def toast(status, content):
    toast = [f'.. admonition:: {status.value.capitalize()}', f'   :class: {status.value}', '', f'   {content}', '']
    return toast

def document_test_methods(app, what, name, obj, options, lines):
    if not callable(obj):
        return False
    if 'pytestmark' in obj.__dict__:
        name = getattr(obj, "__dict__", {})['pytestmark'][0].name
        arg = getattr(obj, "__dict__", {})['pytestmark'][0].args
        if name=='skip':
            lines[:0] = toast(ToastStatus.Skipped, arg[0])
        elif name=='parametrize':
            lines[:0] = toast(ToastStatus.Parametrize, arg)

def setup(app):
    app.connect("autodoc-process-docstring", document_test_methods)
