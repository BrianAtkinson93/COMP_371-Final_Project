# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
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

campus_pic = ('images/ufv-abbotsford-campus-fraser-valley.jpg', './images/ufv-abbotsford-campus-fraser-valley.jpg', 'DATA')
password_pic = ('images/password.png', './images/password.png', 'DATA')
license_plate_pic = ('images/license_plate.png', './images/license_plate.png', 'DATA')
username_pic = ('images/username.png', './images/username.png', 'DATA')

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [campus_pic, password_pic, license_plate_pic, username_pic],
    name='evp.exe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
