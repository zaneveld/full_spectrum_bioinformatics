
"""Create a notebook containing code from a script.
Run as:  python make_nb.py my_script.py
"""
import sys

import nbformat
from nbformat.v4 import new_notebook, new_code_cell

nb = new_notebook()
with open(sys.argv[1]) as f:
    code = f.read()

nb.cells.append(new_code_cell(code))
nbformat.write(nb, sys.argv[1]+'.ipynb')
