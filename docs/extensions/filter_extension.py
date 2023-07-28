def is_test_method(name):
    return name.startswith('test') or name.startswith('Test')

def filter_test_methods(app, what, name, obj, options, lines):
    if is_test_method(name):
        return False
    else:
        return True

def setup(app):
    app.connect("autodoc-skip-member", filter_test_methods)