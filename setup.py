import sys, os
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'
    os.environ['TCL_LIBRARY'] = "C:\\Users\\andrei\\AppData\\Local\\Programs\\Python\\Python36\\DLLs"
    os.environ['TK_LIBRARY'] = "C:\\Users\\andrei\\AppData\\Local\\Programs\\Python\\Python36\\DLLs"

executables = [
    Executable('wxPortfolio.py', base=base)
]

# Dependencies are automatically detected, but might need fine tuning.
build_exe_options = {'packages': ['pandas', 'numpy'],
                     }

setup(name='wxPortfolio',
      version='0.1',
      description='Portfolio management software',
      executables=executables
)
