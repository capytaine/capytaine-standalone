# -*- mode: python ; coding: utf-8 -*-


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
            "ipython",
            "matplotlib",
            "numpy",
            "pandas",
            "scipy",
            "vtk",
            "xarray",
        ],
        hookspath=[],
        hooksconfig={},
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
    [],
    exclude_binaries=True,
    name='ipython-with-capytaine',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ipython-with-capytaine',
)
