from gui import openFileWindow
from gui import getTableWindow
from modules import core

data = openFileWindow.open_file_windows()
_core = core.Core(filepath=data)
df = _core.get_location()
print(df.head(5))
