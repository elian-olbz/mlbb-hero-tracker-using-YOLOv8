# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['heatmap.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/Marlon/anaconda/envs/heatmap/Lib/uuid.py', '.'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/six.py', '.'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/typing_extensions.py', '.'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/pickletools.py', '.'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/ipaddress.py', '.'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/modulefinder.py', '.'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/_markupbase.py', '.'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/ultralytics', 'ultralytics'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/logging', 'logging'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/packaging', 'packaging'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/PIL', 'PIL'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/matplotlib', 'matplotlib'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/pyparsing', 'pyparsing'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/cycler', 'cycler'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/dateutil', 'dateutil'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/kiwisolver', 'kiwisolver'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/importlib_resources', 'importlib_resources'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/zipp', 'zipp'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/mpl_toolkits', 'mpl_toolkits'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/torch', 'torch'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/ctypes', 'ctypes'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/mpmath', 'mpmath'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/tqdm', 'tqdm'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/requests', 'requests'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/urllib3', 'urllib3'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/charset_normalizer', 'charset_normalizer'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/http', 'http'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/idna', 'idna'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/torchvision', 'torchvision'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/html', 'html'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/pandas', 'pandas'),
            ('C:/Users/Marlon/anaconda/envs/heatmap/Lib/site-packages/pytz', 'pytz'),
            ('D:/python_projects/Heatmap/icons', 'icons'),
            ('D:/python_projects/Heatmap/model', 'model'),
            ('D:/python_projects/Heatmap/ui', 'ui'),
            ('D:/python_projects/Heatmap/outputs', 'outputs')
            ],
    hiddenimports=['sympy'],
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
    name='Tracker',
    icon='icon.ico',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
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
    pathex=[],
    strip=False,
    upx=True,
    upx_exclude=[],
    name='heatmap',
)