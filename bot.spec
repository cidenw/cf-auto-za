# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

added_files = [
    ( 'assets/ready-2.png', 'assets' ),
    ( 'assets/start-2.png', 'assets'),
    ( 'assets/join-game.png', 'assets'),
    ( 'assets/cancel.png', 'assets'),
    ( 'assets/confirm.png', 'assets'),
    ( 'assets/ready.png', 'assets'),
    ( 'assets/tab.png', 'assets'),
    ( 'assets/za-confirm.png', 'assets'),
    ( 'assets/za-ok.png', 'assets'),
    ( 'assets/accept.png', 'assets'),
    ( 'assets/3/arcadia/ready.png', 'assets/3/arcadia'),
    ( 'assets/3/arcadia/join.png', 'assets/3/arcadia'),
    ( 'assets/3/arcadia/confirm.png', 'assets/3/arcadia'),
    ( 'assets/3/arcadia/ok.png', 'assets/3/arcadia'),
    ( 'assets/3/arcadia/ok2.png', 'assets/3/arcadia'),
]

a = Analysis(['main.py'],
             pathex=['D:\\Projects\\cf-anti-idle'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='bot',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None, 
          uac_admin=True,
          entitlements_file=None , version='file_version_info.txt', icon='app.ico')
