pip install sphinx
pip install sphinx-rtd-theme
pip install --upgrade myst-parser
sphinx-quickstart
cd .. & sphinx-apidoc -o docs . & cd docs & make clean & .\make.bat html
cd docs & make clean & .\make.bat html

