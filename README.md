# PyXex
A module that allows interatction with the xbox 360 executable format (xex)

Sample Uses

x = Xex('path\to\file\file.xex')
print(hex(x.entry_point))

Usage
README.md
python3 xex-tool.py thisfile.xex

Prerequisites

pip3 install pycrypto

Acknowledgements

Forked from: https://github.com/crobject/PyXex

Research used from:
https://github.com/benvanik/Xenia
https://github.com/xqemu
https://github.com/xqemu/nxdk
http://openxdk.sourceforge.net/
