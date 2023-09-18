#!/usr/bin/env python

import capytaine as cpt

import xarray as xr
xr.__version__ = "9999"  # https://github.com/pydata/xarray/issues/8200

from traitlets.config import Config
c = Config()
c.InteractiveShellApp.exec_lines = [
        "import capytaine",
        "import capytaine as cpt",
]
c.InteractiveShell.banner2 = "\n".join(["import capytaine as cpt", ""])

import IPython
IPython.start_ipython(config=c)
