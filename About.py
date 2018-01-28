#!/usr/bin/env python

import sys

import wx
import wx.html
import wx.lib.wxpTag

#---------------------------------------------------------------------------

class MyAboutBox(wx.Dialog):
    text = '''
<html>
<body bgcolor="#AC76DE">
<center><table bgcolor="#458154" width="100%%" cellspacing="0"
cellpadding="0" border="1">
<tr>
    <td align="center">
    <h1>wxPortfolio %s</h1>
    (%s)<br>
    Running on Python %s<br>
    </td>
</tr>
</table>

<p><b>wxPortfolio</b> is a Python GUI toolkit for investment portfolio management. It is implemented on top of wxPython.</p>

<p><b>wxPortfolio</b> is written by <b>Andrei Radulescu-Banu</b>, Copyright (c) 2018 and is released under an MIT license.</p>

<p><b>wxPython</b> is brought to you by <b>Robin Dunn</b> and<br>
<b>Total Control Software,</b> Copyright (c) 1997-2017.</p>

<p>
<font size="-1">Please see <i>LICENSE</i> for licensing information.</font>
</p>

<p><wxp module="wx" class="Button">
    <param name="label" value="Okay">
    <param name="id" value="ID_OK">
</wxp></p>
</center>
</body>
</html>
'''
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, -1, 'About the wxPython demo',)
        html = wx.html.HtmlWindow(self, -1, size=(420, -1))
        if "gtk2" in wx.PlatformInfo or "gtk3" in wx.PlatformInfo:
            html.SetStandardFonts()
        py_version = sys.version.split()[0]
        txt = self.text % (wx.VERSION_STRING,
                           ", ".join(wx.PlatformInfo[1:]),
                           py_version
                           )
        html.SetPage(txt)
        btn = html.FindWindowById(wx.ID_OK)
        ir = html.GetInternalRepresentation()
        html.SetSize( (ir.GetWidth()+25, ir.GetHeight()+25) )
        self.SetClientSize(html.GetSize())
        self.CentreOnParent(wx.BOTH)

#---------------------------------------------------------------------------



if __name__ == '__main__':
    app = wx.App()
    dlg = MyAboutBox(None)
    dlg.ShowModal()
    dlg.Destroy()
    app.MainLoop()

