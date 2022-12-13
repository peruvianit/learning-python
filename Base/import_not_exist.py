'''
example for the management of a non-existent library

__author__ = "Peruvianit"
__version__ = "1.0.0"
__email__ = "sergioarellanodiaz@gmail.com"
__status__ = "Personal"
'''

import warnings

try:
    import library_non_exist
except ImportError as e:
    library_non_exist = None
    warnings.warn('The library_non_existent package is not installed.')

def call_library_with_errors():
    if library_non_exist is None:
        raise NotImplementedError(
            "Cannot execute the program because the <library_non_exist> package is not installed.\n execute -> pip install <library_non_exist>"
        )




