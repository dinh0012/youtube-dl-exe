# Install packages
`pip install -r requirements.txt`

Note: `PyQt5Designer` and `pyqt5-tools` are only available on Windows

# Install on Ubuntun
`sudo apt install pyqt5-dev-tools pyqt5-dev qttools5-dev-tools`

open Designer: `qtchooser -run-tool=designer -qt=5`

`binary location: site-packages/PyQt5/Qt/bin/designer.exe`

# convert to .ui to .python
pyuic5 yuotube-dl.ui -o mydesign.py
# document 
https://doc.qt.io/qtforpython
# run 
`python main.py`