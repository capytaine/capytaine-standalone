#!/usr/bin/env python

import capytaine as cpt

from traitlets.config import Config
c = Config()
c.InteractiveShellApp.exec_lines = [
        "import capytaine",
        "import capytaine as cpt",
]
c.InteractiveShell.banner2 = "\n".join(["import capytaine as cpt", ""])

import IPython
IPython.start_ipython(config=c)
