# -*- mode: python ; coding: utf-8 -*-

import sys

if sys.platform == "linux":
    os_name = "linux"
elif sys.platform == "darwin":
    os_name = "macos"
elif sys.platform == "win32":
    os_name = "windows"

block_cipher = None


a = Analysis(
        ['ipython-with-capytaine.py'],
        pathex=[],
        binaries=[],
        datas=[],
        hiddenimports=[
            "capytaine",
            "capytaine.green_functions",
            "capytaine.green_functions.libs",
            "capytaine.green_functions.libs.Delhommeau_float32",
            "capytaine.green_functions.libs.Delhommeau_float64",
            "capytaine.green_functions.libs.XieDelhommeau_float32",
            "capytaine.green_functions.libs.XieDelhommeau_float64",
            "IPython",
            "matplotlib",
            "numpy",
            "pandas",
            "scipy",
            "vtk",
            "xarray",
        ],
        hookspath=[],
        hooksconfig={
            "matplotlib": {
                "backends": "all",  # collect all backends
                # "backends": ["TkAgg", "Qt5Agg"],  # collect multiple backends
        },
    },
        runtime_hooks=[],
        excludes=[],
        win_no_prefer_redirects=False,
        win_private_assemblies=False,
        cipher=block_cipher,
        noarchive=False,
        )
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ipython-with-capytaine-' + os_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
