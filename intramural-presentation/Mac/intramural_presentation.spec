# -*- mode: python -*-

block_cipher = None


a = Analysis(['intramural_presentation.py'],
             pathex=['/Users/brandenarnold/stash/boater-exam/intramural-presentation'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='intramural_presentation',
          debug=False,
          strip=False,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='intramural_presentation.app',
             icon=None,
             bundle_identifier=None)
