# Flask Merge DF
#### *A simple web app created with Python 3.10 and Flask 2.1*

Merge your data frames with this web app built in Python with the Flask microframework.
![image](https://raw.githubusercontent.com/metalpoch/flask_merge_df/main/static/imgs/example.gif)

## Features
- Upload your dataframes
- Select the columns and type of merge
- Magic
- Export document as Excel

## Tech
This web app uses a number of open source projects to work properly:

- [Flask] - Microframework written in Python and designed to facilitate the development of MVC web apps.
- [Jinja2] - Jinja2 is a full-featured template engine for Python.
- [Werkzeug] - Werkzeug is a comprehensive WSGI web application library.
- [Pandas] - Easy-to-use data structures and data analysis tools for the Python programming language.
- [Numpy] - NumPy brings the computational power of languages like C and Fortran to Python.
- [Openpyxl] -Is a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.
- [Bootswatch] - A collection of open source themes for Bootstrap.
- [Sweetalert2] - A beautiful, responsive, customizable, accessible replacement for JavaScript's popup boxes.
 
## Installation
##### Clone this repository [GitHub]
```bash
git clone https://github.com/metalpoch/flask_merge_df
cd flask_merge_df/
```
##### Create a virtual environment
```Bash
virtualenv venv
source venv/bin/activate
```
or
```Bash
python -m venv venv
source venv/bin/activate
```

##### Use [pip] to install the modules in the file requirements.txt 
```bash
pip install -r requirements.txt
```

## Use
##### Using flask run
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

##### Using app.run()
```bash
python app.py
```

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:5000
```

## Licence
[MIT]

[//]: #
   [Pandas]: <https://pandas.pydata.org/docs/index.html>
   [Flask]: <https://flask.palletsprojects.com/en/2.1.x/>
   [Werkzeug]: <https://palletsprojects.com/p/werkzeug/>
   [Jinja2]: <https://palletsprojects.com/p/jinja/>
   [Openpyxl]: <https://openpyxl.readthedocs.io/en/stable/>
   [Numpy]: <https://numpy.org/>
   [Sweetalert2]: <https://sweetalert2.github.io/>
   [Bootswatch]: <https://bootswatch.com/>
   [GitHub]: <https://github.com/metalpoch/flask_merge_df>
   [pip]: <https://pip.pypa.io/en/stable/>
   [MIT]: <https://choosealicense.com/licenses/mit/>
