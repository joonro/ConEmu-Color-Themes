# -*- coding: utf-8 -*-
"""
    gen_theme
    ~~~~~~~~~

    ConEmu theme generator

    :copyright: (c) 2015 - 2016 by Radmon.
"""

import re

# This is a demo color scheme
palette = [
'#282a48', # Black
'#5443bc', # DarkBlue
'#66de3d', # DarkGreen
'#77d6fb', # DarkCyan
'#ee3c3c', # DarkRed
'#dd93f9', # DarkMagenta
'#ffb86c', # DarkYellow
'#e4e4de', # Gray
'#9a9a96', # DarkGray
'#6272c4', # Blue
'#50fa7b', # Green
'#8be9fd', # Cyan
'#ff5555', # Red
'#ff79c6', # Magenta
'#fcfc8c', # Yellow
'#f8f8f2', # White

'#000000', # Black
'#000080', # DarkBlue
'#008000', # DarkGreen
'#008080', # DarkCyan
'#800000', # DarkRed
'#800080', # DarkMagenta
'#808000', # DarkYellow
'#c0c0c0', # Gray
'#808080', # DarkGray
'#0000ff', # Blue
'#00ff00', # Green
'#00ffff', # Cyan
'#ff0000', # Red
'#ff00ff', # Magenta
'#ffff00', # Yellow
'#ffffff', # White
]

line = '<value name="ColorTable{0:02}" type="dword" data="00{3}{2}{1}"/>'


def get_rgb(color):
    m = re.match(r'#([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})', color)
    if m is None:
        raise RuntimeError('Invalid color: %s' % color)
    else:
        return m.groups()


def gen_theme():
    for i in range(0, len(palette)):
        color = palette[i]
        r, g, b = map(lambda x: x.lower(), get_rgb(color))
        yield line.format(i, r, g, b)


if __name__ == '__main__':
    out = '\n'.join(gen_theme())
    print(out)
