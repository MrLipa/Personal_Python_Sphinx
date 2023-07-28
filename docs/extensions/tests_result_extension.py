import pandas as pd

data = pd.read_csv('TestResult.csv')
data = data.drop([0, 1]).reset_index(drop=True)

def create_test_result_dict(row):
    test_dict = {}
    for col in data.columns[3:]:
        test_number = int(col)
        test_result = row[col]
        test_dict[test_number] = test_result
    return test_dict

data['Test_Results'] = data.apply(create_test_result_dict, axis=1)
data['Combined'] = data["Package"] + '.' + data["Class"] + '.' + data["Test"]


def get_graph(data):
    method="""
.. plot::

    import matplotlib.pyplot as plt

    test_results = """+str(data)+"""

    colors = {"FAILED": "red", "PASSED": "green", "SKIPPED": "yellow"}
    
    plt.figure(figsize=(6.4, 2.4))

    for i, result in enumerate(test_results.values()):
        plt.scatter(i, 0, c=colors[result], s=100, edgecolors='black')

    plt.xticks(range(len(test_results)), test_results.keys())
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.title("Test results")
    plt.show()
    """
    graph = method.split('\n')
    return graph

def is_test_method(name):
    return name.split('.')[-1].startswith('test')

def append_test_result(app, what, name, obj, options, lines):
    global data
    test_path="tests.tests_frontend.tests_automatic.tests_regression."+".".join(str(elem) for elem in name.split(".")[-4:])+"[chrome]"
    row = data.loc[data['Combined'] == test_path]
    if not callable(obj) or not is_test_method(name) or what!='method' or row.empty:
        return False
    test_data = list(row['Test_Results'])[0]
    lines.extend(get_graph(test_data))

def setup(app):
    app.connect("autodoc-process-docstring", append_test_result)
