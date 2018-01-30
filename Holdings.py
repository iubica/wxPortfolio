#!/usr/bin/env python
#	Tags: phoenix-port, py3-port

import wx
import wx.dataview as dv
import os, sys
import csv
import pandas as pd

# The tickers dataframe
_tickers_df = None

#---------------------------------------------------------------------------

def GetHoldings():
    tickerscrape_env = "TICKERSCRAPE_HOME"
    tickerscrape_home = None

    # Get the home directory of the application
    if tickerscrape_env in os.environ:
        tickerscrape_home = os.environ[tickerscrape_env]
    if not tickerscrape_home:
        if os.name == "posix":
            tickerscrape_home = "/opt/tickerscrape"
        elif os.name == "nt":
            tickerscrape_home = os.environ["APPDATA"] + "\\tickerscrape"
            
    try:
        os.stat(tickerscrape_home)
    except:
        try:
            os.mkdir(tickerscrape_home)
        except IOError as e:
            print(e)
            return None

    # Get the holdings table
    global _tickers_df
    _tickers_df = pd.read_csv(tickerscrape_home + "/tickers.csv")
    _tickers_df.fillna("", inplace=True)
    #print(_tickers_df)
    
def SaveHoldings():
    tickerscrape_env = "TICKERSCRAPE_HOME"
    tickerscrape_home = None

    # Get the home directory of the application
    if tickerscrape_env in os.environ:
        tickerscrape_home = os.environ[tickerscrape_env]
    if not tickerscrape_home:
        if os.name == "posix":
            tickerscrape_home = "/opt/tickerscrape"
        elif os.name == "nt":
            tickerscrape_home = os.environ["APPDATA"] + "\\tickerscrape"
            
    try:
        os.stat(tickerscrape_home)
    except:
        try:
            os.mkdir(tickerscrape_home)
        except IOError as e:
            print(e)
            return None

    # Get the holdings table
    global _tickers_df

    # Save the holdings table
    df = _tickers_df.set_index("Ticker", inplace=False)
    df.to_csv(tickerscrape_home + "/tickers_out.csv")
    


#----------------------------------------------------------------------

# This model class provides the data to the view when it is asked for.
# Since it is a list-only model (no hierarchical data) then it is able
# to be referenced by row rather than by item object, so in this way
# it is easier to comprehend and use than other model types.  In this
# example we also provide a Compare function to assist with sorting of
# items in our model.  Notice that the data items in the data model
# object don't ever change position due to a sort or column
# reordering.  The view manages all of that and maps view rows and
# columns to the model's rows and columns as needed.
#
# For this example our data is stored in a simple list of lists.  In
# real life you can use whatever you want or need to hold your data.

class TestModel(dv.DataViewIndexListModel):
    def __init__(self, data, log):
        dv.DataViewIndexListModel.__init__(self, len(data))
        self.data = data
        self.log = log

    # All of our columns are strings.  If the model or the renderers
    # in the view are other types then that should be reflected here.
    def GetColumnType(self, col):
        return "string"

    # This method is called to provide the data object for a
    # particular row,col
    def GetValueByRow(self, row, col):        
        self.log.write("GetValue: (%d,%d) %s\n" % (row, col, self.data.iloc[row, col]))
        return self.data.iloc[row, col]

    # This method is called when the user edits a data item in the view.
    def SetValueByRow(self, value, row, col):
        self.log.write("SetValue: (%d,%d) %s\n" % (row, col, value))
        self.data.iloc[row, col] = value
        return True

    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return self.data.num_columns

    # Report the number of rows in the model
    def GetCount(self):
        #self.log.write('GetCount')
        return self.data.count + 1

    # Called to check if non-standard attributes should be used in the
    # cell at (row, col)
    def GetAttrByRow(self, row, col, attr):
        ##self.log.write('GetAttrByRow: (%d, %d)' % (row, col))
        if col == 3:
            attr.SetColour('blue')
            attr.SetBold(True)
            return True
        return False


    # This is called to assist with sorting the data in the view.  The
    # first two args are instances of the DataViewItem class, so we
    # need to convert them to row numbers with the GetRow method.
    # Then it's just a matter of fetching the right values from our
    # data set and comparing them.  The return value is -1, 0, or 1,
    # just like Python's cmp() function.
    def Compare(self, item1, item2, col, ascending):
        if not ascending: # swap sort order?
            item2, item1 = item1, item2
        row1 = self.GetRow(item1)
        row2 = self.GetRow(item2)
        if col == 0:
            return cmp(int(self.data.iloc[row1, col]), int(self.data.iloc[row2, col]))
        else:
            return cmp(self.data.iloc[row1, col], self.idata[row2, col])


    def DeleteRows(self, rows):
        # make a copy since we'll be sorting(mutating) the list
        rows = list(rows)
        # use reverse order so the indexes don't change as we remove items
        rows.sort(reverse=True)

        for row in rows:
            # remove it from our data structure
            del self.data[row]
            # notify the view(s) using this model that it has been removed
            self.RowDeleted(row)


    def AddRow(self, value):
        # update data structure
        self.data.append(value)
        # notify views
        self.RowAppended()



class TestPanel(wx.Panel):
    def __init__(self, parent, log, model=None, data=None):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        # Create a dataview control
        self.dvc = dv.DataViewCtrl(self,
                                   style=wx.BORDER_THEME
                                   | dv.DV_ROW_LINES # nice alternating bg colors
                                   #| dv.DV_HORIZ_RULES
                                   | dv.DV_VERT_RULES
                                   | dv.DV_MULTIPLE
                                   )

        # Create an instance of our simple model...
        if model is None:
            self.model = TestModel(data, log)
        else:
            self.model = model

        # ...and associate it with the dataview control.  Models can
        # be shared between multiple DataViewCtrls, so this does not
        # assign ownership like many things in wx do.  There is some
        # internal reference counting happening so you don't really
        # need to hold a reference to it either, but we do for this
        # example so we can fiddle with the model from the widget
        # inspector or whatever.
        self.dvc.AssociateModel(self.model)

        # Now we create some columns.  The second parameter is the
        # column number within the model that the DataViewColumn will
        # fetch the data from.  This means that you can have views
        # using the same model that show different columns of data, or
        # that they can be in a different order than in the model.
        self.dvc.AppendTextColumn("Ticker", 0, width=60, 
                                  mode=dv.DATAVIEW_CELL_EDITABLE)
        self.dvc.AppendTextColumn("Name", 1, width=260)
        self.dvc.AppendTextColumn("Shares", 2, width=80, 
                                  mode=dv.DATAVIEW_CELL_EDITABLE)
        self.dvc.AppendTextColumn("Cost Basis", 3, width=100, 
                                  mode=dv.DATAVIEW_CELL_EDITABLE)
        self.dvc.AppendTextColumn("Purchase Date", 4, width=100, 
                                  mode=dv.DATAVIEW_CELL_EDITABLE)

        # Through the magic of Python we can also access the columns
        # as a list via the Columns property.  Here we'll mark them
        # all as sortable and reorderable.
        for c in self.dvc.Columns:
            c.Sortable = True
            c.Reorderable = True

        # set the Sizer property (same as SetSizer)
        self.Sizer = wx.BoxSizer(wx.VERTICAL)
        self.Sizer.Add(self.dvc, 1, wx.EXPAND)

        # Add some buttons to help out with the tests
        b1 = wx.Button(self, label="New View", name="newView")
        self.Bind(wx.EVT_BUTTON, self.OnNewView, b1)
        b2 = wx.Button(self, label="Add Row")
        self.Bind(wx.EVT_BUTTON, self.OnAddRow, b2)
        b3 = wx.Button(self, label="Delete Row(s)")
        self.Bind(wx.EVT_BUTTON, self.OnDeleteRows, b3)

        btnbox = wx.BoxSizer(wx.HORIZONTAL)
        btnbox.Add(b1, 0, wx.LEFT|wx.RIGHT, 5)
        btnbox.Add(b2, 0, wx.LEFT|wx.RIGHT, 5)
        btnbox.Add(b3, 0, wx.LEFT|wx.RIGHT, 5)
        self.Sizer.Add(btnbox, 0, wx.TOP|wx.BOTTOM, 5)

        # Bind some events so we can see what the DVC sends us
        self.Bind(dv.EVT_DATAVIEW_ITEM_EDITING_DONE, self.OnEditingDone, self.dvc)
        self.Bind(dv.EVT_DATAVIEW_ITEM_VALUE_CHANGED, self.OnValueChanged, self.dvc)


    def OnNewView(self, evt):
        f = wx.Frame(None, title="New view, shared model", size=(600,400))
        TestPanel(f, self.log, self.model)
        b = f.FindWindowByName("newView")
        b.Disable()
        f.Show()


    def OnDeleteRows(self, evt):
        # Remove the selected row(s) from the model. The model will take care
        # of notifying the view (and any other observers) that the change has
        # happened.
        items = self.dvc.GetSelections()
        rows = [self.model.GetRow(item) for item in items]
        self.model.DeleteRows(rows)


    def OnAddRow(self, evt):
        # Add some bogus data to a new row in the model's data
        id = len(self.model.data) + 1
        value = [str(id),
                 'new artist %d' % id,
                 'new title %d' % id,
                 'genre %d' % id]
        self.model.AddRow(value)


    def OnEditingDone(self, evt):
        self.log.write("OnEditingDone\n")

    def OnValueChanged(self, evt):
        self.log.write("OnValueChanged\n")


#----------------------------------------------------------------------

def runTest(frame, nb, log):

    GetHoldings()

    # Get the data from the ListCtrl sample to play with, converting it
    # from a dictionary to a list of lists, including the dictionary key
    # as the first element of each sublist.
    import ListCtrl
    musicdata = sorted(ListCtrl.musicdata.items())
    musicdata = [[str(k)] + list(v) for k,v in musicdata]

    win = TestPanel(nb, log, data=_tickers_df)
    return win

#----------------------------------------------------------------------



overview = """<html><body>
<h2><center>DataViewCtrl with DataViewIndexListModel</center></h2>

This sample shows how to derive a class from PyDataViewIndexListModel and use
it to interface with a list of data items. (This model does not have any
hierarchical relationships in the data.)

<p> See the comments in the source for lots of details.

</body></html>
"""



if __name__ == '__main__':
    import sys,os
    import run
    run.main(['', os.path.basename(sys.argv[0])] + sys.argv[1:])
