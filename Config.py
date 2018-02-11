# viewdata.py

"""
Globals for the main.py wxPython views.
"""

import wx
import pandas as pd
import Main

#-------------------------------------------------------------------------------
#
# viewPngs
#
# These are the images names used in the wxPortfolio treectrl.
# These come from images.py or bitmaps/imagename.ext
#
# viewPngs = ["imagename1", "imagename2", "etc"]
#
#-------------------------------------------------------------------------------

viewPngs = ["overview", # Top level views
            "custom", # Portfolio
            "custom", # Performance
            "custom", # Config
            "recent", # Recent Additions/Updates
            "frame",  # ...
            "dialog", 
            "moredialog", 
            "core",
            "book", 
            "customcontrol", 
            "morecontrols", 
            "layout", 
            "process",
            "clipboard", 
            "images", 
            "miscellaneous"]


#-------------------------------------------------------------------------------
#
# viewTree
#
# These are the View Catagory Headers
# and View Module Names(Ex: Frame.py without ext)
#
# ('View Category Name', [
#       'ViewModuleName1',
#       'ViewModuleName2',
#       'Etc',
#       ]),
#
# The ViewModuleName should correspond to a ViewModuleName.py file in the
# top folder, with the following globals and methods:
#   overview - HTML string showing in the Help tab 
#   runTest(frame, nb, log) - returns panel object for module
#
#-------------------------------------------------------------------------------

viewTree = [
    # portfolio views
    ('Portfolio', [
        'Holdings',
        'Accounts',
    ]),

    ('Performance', [
        'PerformanceHistory',
        'TrailingTotalReturns',
    ]),

    ('Config', [
        'AccountTypes',
        'Categories',
    ]),

    # new stuff
    ('Recent Additions/Updates', [
        'FileCtrl',
        'Overlay',
        'RearrangeDialog',
        'RichMessageDialog',
        'ToolTip',
        'TimePickerCtrl',
        'BannerWindow',
    ]),

    # managed windows == things with a (optional) caption you can close
    ('Frames and Dialogs', [
        'AUI_DockingWindowMgr',
        'AUI_MDI',
        'Dialog',
        'Frame',
        'MDIWindows',
        'MiniFrame',
        'Wizard',
    ]),

    # the common dialogs
    ('Common Dialogs', [
        'AboutBox',
        'ColourDialog',
        'DirDialog',
        'FileDialog',
        'FindReplaceDialog',
        'FontDialog',
        'MessageDialog',
        'MultiChoiceDialog',
        'PageSetupDialog',
        'PrintDialog',
        'ProgressDialog',
        'SingleChoiceDialog',
        'TextEntryDialog',
        'RearrangeDialog',
        'RichMessageDialog',
        'NotificationMessage',
        'RichToolTip',
    ]),

    # dialogs from libraries
    ('More Dialogs', [
        'ImageBrowser',
        'ScrolledMessageDialog',
    ]),

    # core controls
    ('Core Windows/Controls', [
        'BitmapButton',
        'Button',
        'CheckBox',
        'CheckListBox',
        'Choice',
        'ComboBox',
        'CommandLinkButton',
        'DVC_CustomRenderer',
        'DVC_DataViewModel',
        'DVC_IndexListModel',
        'DVC_ListCtrl',
        'DVC_TreeCtrl',
        'Gauge',
        'Grid',
        'Grid_MegaExample',
        'GridLabelRenderer',
        'ListBox',
        'ListCtrl',
        'ListCtrl_virtual',
        'ListCtrl_edit',
        'Menu',
        'PopupMenu',
        'PopupWindow',
        'RadioBox',
        'RadioButton',
        'SashWindow',
        'ScrolledWindow',
        'SearchCtrl',
        'Slider',
        'SpinButton',
        'SpinCtrl',
        'SpinCtrlDouble',
        'SplitterWindow',
        'StaticBitmap',
        'StaticBox',
        'StaticText',
        'StatusBar',
        'StockButtons',
        'TextCtrl',
        'ToggleButton',
        'ToolBar',
        'TreeCtrl',
        'Validator',
    ]),

    ('"Book" Controls', [
        'AUI_Notebook',
        'Choicebook',
        'FlatNotebook',
        'Listbook',
        'Notebook',
        'Toolbook',
        'Treebook',
    ]),

    ('Custom Controls', [
        'AnalogClock',
        'ColourSelect',
        'ComboTreeBox',
        'Editor',
        'FileCtrl',
        'GenericButtons',
        'GenericDirCtrl',
        'ItemsPicker',
        #'LEDNumberCtrl',  # TODO
        'MultiSash',
        'PlateButton',
        'PopupControl',
        'PyColourChooser',
        'TreeListCtrl',  # TODO or toss it?
    ]),

    # controls coming from other libraries
    ('More Windows/Controls', [
        'ActiveX_FlashWindow',
        'ActiveX_IEHtmlWindow',
        'ActiveX_PDFWindow',
        'BitmapComboBox',
        'Calendar',
        'CalendarCtrl',
        'CheckListCtrlMixin',
        'CollapsiblePane',
        'ComboCtrl',
        'ContextHelp',
        'DatePickerCtrl',
        #'DynamicSashWindow',  # TODO
        'EditableListBox',
        'ExpandoTextCtrl',
        'FancyText',
        'FileBrowseButton',
        'FloatBar',
        'FloatCanvas',
        'HtmlWindow',
        'HTML2_WebView',
        'InfoBar',
        'IntCtrl',
        'MaskedEditControls',
        'MaskedNumCtrl',
        'MediaCtrl',
        'MultiSplitterWindow',
        'OwnerDrawnComboBox',
        'Pickers',
        'PropertyGrid',
        'PyCrust',
        'PyPlot',
        'PyShell',
        'ResizeWidget',
        'RichTextCtrl',
        'ScrolledPanel',
        #'SplitTree',         # TODO or toss it?
        'StyledTextCtrl_1',
        'StyledTextCtrl_2',
        'TablePrint',
        'Throbber',
        'Ticker',
        'TimeCtrl',
        'TimePickerCtrl',
        'TreeMixin',
        'VListBox',
    ]),

    # How to lay out the controls in a frame/dialog
    ('Window Layout', [
        'GridBagSizer',
        'LayoutAnchors',
        'LayoutConstraints',
        'Layoutf',
        'ScrolledPanel',
        'SizedControls',
        'Sizers',
        'WrapSizer',
        'XmlResource',
        'XmlResourceHandler',
        'XmlResourceSubclass',
    ]),

    # ditto
    ('Process and Events', [
        'DelayedResult',
        'EventManager',
        'KeyEvents',
        'Process',
        'PythonEvents',
        'Threads',
        'Timer',
        ##'infoframe',    # needs better explanation and some fixing
    ]),

    # Clipboard and DnD
    ('Clipboard and DnD', [
        'CustomDragAndDrop',
        'DragAndDrop',
        'URLDragAndDrop',
    ]),

    # Images
    ('Using Images', [
        'AdjustChannels',
        'AlphaDrawing',
        'AnimateCtrl',
        'ArtProvider',
        'BitmapFromBuffer',
        'Cursor',
        'DragImage',
        'Image',
        'ImageAlpha',
        'ImageFromStream',
        'Img2PyArtProvider',
        'Mask',
        'RawBitmapAccess',
        'Throbber',
    ]),

    # Other stuff
    ('Miscellaneous', [
        'AlphaDrawing',
        'BannerWindow',
        'Cairo',
        'Cairo_Snippets',
        'ColourDB',
        ##'DialogUnits',   # needs more explanations
        'DragScroller',
        'DrawXXXList',
        'FileHistory',
        'FontEnumerator',
        'GetMouseState',
        'GraphicsContext',
        'GraphicsGradient',
        'GLCanvas',
        'I18N',
        'Joystick',
        'MimeTypesManager',
        'MouseGestures',
        'OGL',
        'Overlay',
        'PDFViewer',
        'PenAndBrushStyles',
        'PrintFramework',
        'PseudoDC',
        'RendererNative',
        'ShapedWindow',
        'Sound',
        'StandardPaths',
        'SystemSettings',
        'ToolTip',
        'UIActionSimulator',
        'Unicode',
    ]),

    ('Check out the samples dir too', []),

]

#---------------------------------------------------------------------------
# Get the entire portfolio
def PortfolioRead():
    HoldingsRead()
    AccountsRead()
    AccountTypesRead()
    CategoriesRead()

#---------------------------------------------------------------------------
# Save the entire portfolio
def PortfolioSave():
    HoldingsSave()
    AccountsSave()
    AccountTypesSave()
    CategoriesSave()

#---------------------------------------------------------------------------
# Called with changed = True or False when holdings are different (or unchanged)
# from the holdings.csv, and called with changed = None to just return
# the status of the holdings (whether they have changed or not)

def PortfolioChanged():
    return _holdingsChanged or _accountsChanged or _accountTypesChanged or _categoriesChanged

#---------------------------------------------------------------------------

# The holdings dataframe
holdingsDf = None
_holdingsChanged = False

#---------------------------------------------------------------------------
# Get portfolio holdings from holdings.csv

def HoldingsRead():
    # Get the wxPython standard paths
    sp = wx.StandardPaths.Get()

    # Get the global holdings table
    global holdingsDf

    try:
        holdingsDf = pd.read_csv(sp.GetUserDataDir() + "/holdings.csv")

        HoldingsChanged(False)
    except OSError as e:
        # Create an empty DataFrame with unordered columns
        holdingsDf = pd.DataFrame.from_dict({
            "Account": ["", ""],
            "Ticker": ["SPY", "FUSEX"],
            "Shares": ["100", "150"],
            "Cost Basis": ["150000.00", "100.00"],
            "Purchase Date": ["2/3/2011", "2/4/2011"]
        })
        
        # Order the columns
        holdingsDf = holdingsDf[["Account",
                                 "Ticker", 
                                 "Shares", 
                                 "Cost Basis", 
                                 "Purchase Date"]]

        # Holdings have been modified
        HoldingsChanged(True)

    holdingsDf.fillna("", inplace=True)
    #print(holdingsDf)

#---------------------------------------------------------------------------
# Save portfolio holdings to holdings.csv

def HoldingsSave():
    # Get the wxPython standard paths
    sp = wx.StandardPaths.Get()

    # Save the holdings table
    df = holdingsDf.set_index("Account", inplace=False)    
    df.to_csv(sp.GetUserDataDir() + "/holdings.csv")

    # Holdings are now in sync
    HoldingsChanged(False)

#---------------------------------------------------------------------------
# Called with changed = True or False when holdings are different (or unchanged)
# from the holdings.csv, and called with changed = None to just return
# the status of the holdings (whether they have changed or not)

def HoldingsChanged(changed):
    global _holdingsChanged

    if changed is not None:
        if Main.portfolioFrame:
            Main.portfolioFrame.EnableFileMenuSaveItem(changed)
        _holdingsChanged = changed

    return _holdingsChanged


#---------------------------------------------------------------------------

# The accounts dataframe
accountsDf = None
_accountsChanged = False

#---------------------------------------------------------------------------
# Get portfolio accounts from accounts.csv

def AccountsRead():
    # Get the wxPython standard paths
    sp = wx.StandardPaths.Get()

    # Get the global accounts table
    global accountsDf

    try:
        accountsDf = pd.read_csv(sp.GetUserDataDir() + "/accounts.csv")

        AccountsChanged(False)
    except OSError as e:
        # Create an empty DataFrame with unordered columns
        accountsDf = pd.DataFrame.from_dict({
            "Account Name": ["Account One", "Account Two"],
            "Account Number": ["100", "101"],
            "Type": ["Brokerage", "401K"],
        })
        
        # Order the columns
        accountsDf = accountsDf[["Account Name", 
                                 "Account Number", 
                                 "Type"]]

        # Accounts have been modified
        AccountsChanged(True)

    accountsDf.fillna("", inplace=True)
    #print(accountsDf)

#---------------------------------------------------------------------------
# Save portfolio accounts to accounts.csv

def AccountsSave():
    # Get the wxPython standard paths
    sp = wx.StandardPaths.Get()

    # Save the accounts table
    df = accountsDf.set_index("Account Name", inplace=False)    
    df.to_csv(sp.GetUserDataDir() + "/accounts.csv")

    # Accounts are now in sync
    AccountsChanged(False)

#---------------------------------------------------------------------------
# Called with changed = True or False when accounts are different (or unchanged)
# from the accounts.csv, and called with changed = None to just return
# the status of the accounts (whether they have changed or not)

def AccountsChanged(changed):
    global _accountsChanged

    if changed is not None:
        if Main.portfolioFrame:
            Main.portfolioFrame.EnableFileMenuSaveItem(changed)
        _accountsChanged = changed

    return _accountsChanged

#---------------------------------------------------------------------------
def AccountList():
    return accountsDf.ix[:,"Account Name"].tolist()

#---------------------------------------------------------------------------
def AccountFind(acct):
    if acct in AccountList():
        return True
    return False

#---------------------------------------------------------------------------
def AccountChange(acctOld, acctNew):
    acctChanged = False
    holdingsChanged = False

    if AccountFind(acctNew):
        return False, "Account '%s' already configured" % acctNew

    for i in range(accountsDf.shape[0]):
        if accountsDf.ix[i,"Account Name"] == acctOld:
            accountsDf.ix[i,"Account Name"] = acctNew
            acctChanged = True

    if not acctChanged:
        return False, "Account '%s' does not exist" % acctOld

    # Also change the holdings
    for i in range(holdingsDf.shape[0]):
        if holdingsDf.ix[i,"Account"] == acctOld:
            holdingsDf.ix[i,"Account"] = acctNew
            holdingsChanged = True

    if acctChanged:
        AccountsChanged(True)

    if holdingsChanged:
        HoldingsChanged(True)

    return True, None


#---------------------------------------------------------------------------

# The accounts dataframe
accountTypesDf = None
_accountTypesChanged = False

#---------------------------------------------------------------------------
# Get portfolio account types from accountTypes.csv

def AccountTypesRead():
    # Get the wxPython standard paths
    sp = wx.StandardPaths.Get()

    # Get the global accounts table
    global accountTypesDf

    try:
        accountTypesDf = pd.read_csv(sp.GetUserDataDir() + "/accountTypes.csv")

        AccountTypesChanged(False)
    except OSError as e:
        # Create an empty DataFrame with unordered columns
        accountTypesDf = pd.DataFrame.from_dict({
            "Account Type": ["Brokerage", "401K", "Roth 401K", "IRA", "Roth IRA", "529"],
            "Long Term Capital Gains Tax": ["15%", "", "", "", "", ""],
            "Short Term Capital Gains Tax": ["35%", "", "", "", "", ""],
            "Liquidation Tax": ["", "35%", "", "35%", "", ""],
        })
        
        # Order the columns
        accountTypesDf = accountTypesDf[["Account Type", 
                                         "Long Term Capital Gains Tax", 
                                         "Short Term Capital Gains Tax", 
                                         "Liquidation Tax"]]
        
        # Accounts have been modified
        AccountTypesChanged(True)

    accountTypesDf.fillna("", inplace=True)
    #print(accountsDf)

#---------------------------------------------------------------------------
# Save portfolio account types to accountTypes.csv

def AccountTypesSave():
    # Get the wxPython standard paths
    sp = wx.StandardPaths.Get()

    # Save the accounts table
    df = accountTypesDf.set_index("Account Type", inplace=False)    
    df.to_csv(sp.GetUserDataDir() + "/accountTypes.csv")

    # AccountTypes are now in sync
    AccountTypesChanged(False)

#---------------------------------------------------------------------------
def AccountTypesChanged(changed):
    global _accountTypesChanged

    if changed is not None:
        if Main.portfolioFrame:
            Main.portfolioFrame.EnableFileMenuSaveItem(changed)
        _accountTypesChanged = changed

    return _accountTypesChanged

#---------------------------------------------------------------------------
def AccountTypesList():
    return accountTypesDf.ix[:,"Account Type"].tolist()

#---------------------------------------------------------------------------
def AccountTypesFind(acct):
    if acct in AccountTypesList():
        return True
    return False

#---------------------------------------------------------------------------
def AccountTypesChange(acctTypeOld, acctTypeNew):
    acctTypesChanged = False
    acctChanged = False

    if AccountTypesFind(acctTypeNew):
        return False, "Account type '%s' already configured" % acctTypeNew

    for i in range(accountTypesDf.shape[0]):
        if accountTypesDf.ix[i,"Account Type"] == acctTypeOld:
            accountTypesDf.ix[i,"Account Type"] = acctTypeNew
            acctTypesChanged = True

    if not acctTypesChanged:
        return False, "Account type '%s' does not exist" % acctTypeOld

    # Also change the accounts
    for i in range(accountsDf.shape[0]):
        if accountsDf.ix[i,"Type"] == acctTypeOld:
            accountsDf.ix[i,"Type"] = acctTypeNew
            acctChanged = True

    if acctTypesChanged:
        AccountTypesChanged(True)

    if acctChanged:
        AccountsChanged(True)

    return True, None


#---------------------------------------------------------------------------

# The accounts dataframe
categoriesDf = None
_categoriesChanged = False

#---------------------------------------------------------------------------
# Get categories from categories.csv

def CategoriesRead():
    # Get the wxPython standard paths
    sp = wx.StandardPaths.Get()

    # Get the global accounts table
    global categoriesDf

    try:
        categoriesDf = pd.read_csv(sp.GetUserDataDir() + "/categories.csv")

        CategoriesChanged(False)
    except OSError as e:
        # Create an empty DataFrame with unordered columns
        categoriesDf = pd.DataFrame.from_dict({
            "Category Name": [
                "Large Value", # U.S. Equity
                "Large Blend",
                "Large Growth",
                "Mid-Cap Value",
                "Mid-Cap Blend",
                "Mid-Cap Growth",
                "Small Value",
                "Small Blend",
                "Small Growth",
                "Leveraged Net Long",

                "Communications", # Sector Equity
                "Consumer Cyclical", 
                "Consumer Defensive", 
                "Energy Limited Partnership", 
                "Equity Energy", 
                "Equity Precious Metals", 
                "Financial", 
                "Global Real Estate", 
                "Health", 
                "Industrials", 
                "Natural Resources", 
                "Real Estate", 
                "Technology", 
                "Utilities", 
                "Miscellaneous Sector", 

                "Target Date 2036-2040", # Allocation
                "Target Date 2041-2045", 
                "Target Date 2046-2050", 
                "Target Date 2051+", 
                "Retirement Income", 

                "Foreign Large Value", # International Equity
                "Foreign Large Blend",
                "Foreign Large Growth",
                "Foreign Small/Mid Value",
                "Foreign Small/Mid Blend",
                "Foreign Small/Mid Growth",
                "World Stock",
                "Diversified Emerging Markets",
                "Diversified Pacific/Asia",
                "Miscellaneous Region",
                "Europe Stock",
                "Latin America Stock",
                "Pacific/Asia ex-Japan Stock",
                "China Region",
                "India Equity",
                "Japan Stock",

                "Bear Market", # Alternative
                "Multicurrency",
                "Single Currency",
                "Long/Short Equity",
                "Market Neutral",
                "Multialternative",
                "Managed Futures",
                "Volatility",
                "Trading--Leveraged Commodities",
                "Trading--Inverse Commodities",
                "Trading--Leveraged Debt",
                "Trading--Inverse Debt",
                "Trading--Leveraged Equity",
                "Trading--Inverse Equity",
                "Trading--Miscellaneous",

                "Commodities Agriculture", # Commodities
                "Commodities Broad Basket",
                "Commodities Energy",
                "Commodities Industrial Metals",
                "Commodities Miscellaneous",
                "Commodities Precious Metals",

                "Long Government", # Taxable Bond
                "Intermediate Government",
                "Short Government",
                "Inflation-Protected Bond",
                "Long-Term Bond",
                "Intermediate-Term Bond",
                "Short-Term Bond",
                "Ultrashort Bond",
                "Bank Loan",
                "Stable Value",
                "Corporate Bond",
                "Preferred Stock",
                "High-Yield Bond",
                "Multisector Bond",
                "World Bond",
                "Emerging-Markets Bond",
                "Nontraditional Bond",
                
                "Muni National Long", # Municipal Bond
                "Muni National Intermediate",
                "Muni National Short",
                "High-Yield Muni",
                "Muni Single State Long",
                "Muni Single State Intermediate",
                "Muni Single State Short",
                "Muni California Long",
                "Muni California Intermediate",
                "Muni Massachusetts",
                "Muni Minnesota",
                "Muni New Jersey",
                "Muni New York Long",
                "Muni New York Intermediate",
                "Muni Ohio",
                "Muni Pennsylvania",

                "Taxable Money Market", # Money Market
                "Tax-Free Money Market",
            ],
            "Category Group": [
                "U.S. Equity",
                "U.S. Equity",
                "U.S. Equity",
                "U.S. Equity",
                "U.S. Equity",
                "U.S. Equity",
                "U.S. Equity",
                "U.S. Equity",
                "U.S. Equity",
                "U.S. Equity",

                "Sector Equity", 
                "Sector Equity", 
                "Sector Equity", 
                "Sector Equity", 
                "Sector Equity", 
                "Sector Equity", 
                "Sector Equity", 
                "Sector Equity", 
                "Sector Equity", 
                "Sector Equity", 
                "Sector Equity", 
                "Sector Equity", 
                "Sector Equity", 
                "Sector Equity", 
                "Sector Equity", 

                "Allocation", 
                "Allocation", 
                "Allocation", 
                "Allocation", 
                "Allocation", 

                "International Equity", 
                "International Equity", 
                "International Equity", 
                "International Equity", 
                "International Equity", 
                "International Equity", 
                "International Equity", 
                "International Equity", 
                "International Equity", 
                "International Equity", 
                "International Equity", 
                "International Equity", 
                "International Equity", 
                "International Equity", 
                "International Equity", 
                "International Equity",

                "Alternative",
                "Alternative",
                "Alternative",
                "Alternative",
                "Alternative",
                "Alternative",
                "Alternative",
                "Alternative",
                "Alternative",
                "Alternative",
                "Alternative",
                "Alternative",
                "Alternative",
                "Alternative",
                "Alternative",

                "Commodities",
                "Commodities",
                "Commodities",
                "Commodities",
                "Commodities",
                "Commodities",

                "Taxable Bond",
                "Taxable Bond",
                "Taxable Bond",
                "Taxable Bond",
                "Taxable Bond",
                "Taxable Bond",
                "Taxable Bond",
                "Taxable Bond",
                "Taxable Bond",
                "Taxable Bond",
                "Taxable Bond",
                "Taxable Bond",
                "Taxable Bond",
                "Taxable Bond",
                "Taxable Bond",
                "Taxable Bond",
                "Taxable Bond",

                "Municipal Bond",
                "Municipal Bond",
                "Municipal Bond",
                "Municipal Bond",
                "Municipal Bond",
                "Municipal Bond",
                "Municipal Bond",
                "Municipal Bond",
                "Municipal Bond",
                "Municipal Bond",
                "Municipal Bond",
                "Municipal Bond",
                "Municipal Bond",
                "Municipal Bond",
                "Municipal Bond",
                "Municipal Bond",

                "Money Market",
                "Money Market",
            ],
            "Benchmark ETF": [
                "", # U.S. Equity
                "", 
                "", 
                "", 
                "", 
                "", 
                "", 
                "", 
                "", 
                "", 

                "", # Sector Equity
                "", 
                "", 
                "", 
                "", 
                "", 
                "", 
                "", 
                "", 
                "", 
                "", 
                "", 
                "", 
                "", 
                "", 

                "SPY", # Allocation
                "", 
                "", 
                "", 
                "", 

                "", # International Equity
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",

                "", # Alternative
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",

                "", # Commodities
                "",
                "",
                "",
                "",
                "",

                "", # Taxable Bond
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                
                "", # Municipal Bond
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",

                "", # Money Market
                "",
            ],
        })
        
        # Order the columns
        categoriesDf = categoriesDf[["Category Name", 
                                     "Category Group", 
                                     "Benchmark ETF"]]
        
        # Accounts have been modified
        CategoriesChanged(True)

    categoriesDf.fillna("", inplace=True)
    print(categoriesDf)

#---------------------------------------------------------------------------
# Save categories to categories.csv

def CategoriesSave():
    # Get the wxPython standard paths
    sp = wx.StandardPaths.Get()

    # Save the accounts table
    df = categoriesDf.set_index("Category Name", inplace=False)    
    df.to_csv(sp.GetUserDataDir() + "/categories.csv")

    # AccountTypes are now in sync
    CategoriesChanged(False)

#---------------------------------------------------------------------------
def CategoriesChanged(changed):
    global _categoriesChanged

    if changed is not None:
        if Main.portfolioFrame:
            Main.portfolioFrame.EnableFileMenuSaveItem(changed)
        _categoriesChanged = changed

    return _categoriesChanged

#---------------------------------------------------------------------------
def CategoriesList():
    return categoriesDf.ix[:,"Category Name"].tolist()

#---------------------------------------------------------------------------
def CategoriesFind(acct):
    if acct in CategoriesList():
        return True
    return False

#---------------------------------------------------------------------------
def CategoriesChange(categoryOld, categoryNew):
    categoriesChanged = False

    if CategoriesFind(categoryNew):
        return False, "Category '%s' already configured" % categoryNew

    for i in range(categoriesDf.shape[0]):
        if categoriesDf.ix[i,"Category Name"] == categoryOld:
            categoriesDf.ix[i,"Category Name"] = categoryNew
            categoriesChanged = True

    if not categoriesChanged:
        return False, "Category '%s' does not exist" % categoryOld

    if categoriesChanged:
        CategoriesChanged(True)

    return True, None
