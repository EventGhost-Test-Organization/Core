# -*- coding: utf-8 -*-
#
# This file is part of EventGhost.
# Copyright © 2005-2016 EventGhost Project <http://www.eventghost.org/>
#
# EventGhost is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# EventGhost is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with EventGhost. If not, see <http://www.gnu.org/licenses/>.

import os
import wx
from os.path import exists, join
from time import localtime, strftime
from wx.combo import BitmapComboBox

# Local imports
import eg

INDENT_WIDTH = 18


LANG_NAME_TO_CODE = {
    u'Afrikaans': 'af',
    u'shqiptar': 'sq',
    u'አማርኛ': 'am',
    u'العربية - الجزائر': 'ar-dz',
    u'العربية - البحرين': 'ar-bh',
    u'اللغة العربية - مصر': 'ar-eg',
    u'عربي - العراق': 'ar-iq',
    u'عربي - الاردن': 'ar-jo',
    u'العربية - الكويت': 'ar-kw',
    u'العربية - لبنان': 'ar-lb',
    u'العربية - ليبيا': 'ar-ly',
    u'اللغة العربية - المغرب': 'ar-ma',
    u'العربية - عمان': 'ar-om',
    u'العربية - قطر': 'ar-qa',
    u'العربية - السعودية': 'ar-sa',
    u'العربية - سوريا': 'ar-sy',
    u'العربية - تونس': 'ar-tn',
    u'العربية - الامارات العربية المتحدة': 'ar-ae',
    u'العربية - اليمن': 'ar-ye',
    u'հայերեն': 'hy',
    u'Assamese': 'as',
    u'Azeri - Cyrillic': 'az-az',
    u'Azeri - Latin': 'az-az',
    u'Euskal': 'eu',
    u'беларускі': 'be',
    u'Bosanski': 'bs',
    u'български': 'bg',
    u'Burmese': 'my',
    u'Català': 'ca',
    u'中國 - 香港特別行政區': 'zh-hk',
    u'中國 - 澳門特區': 'zh-mo',
    u'中文 - 新加坡': 'zh-sg',
    u'中文 - 台灣': 'zh-tw',
    u'Hrvatski': 'hr',
    u'čeština': 'cs',
    u'dansk': 'da',
    u'Divehi; Dhivehi; Maldivian': 'dv',
    u'Nederlands': 'nl-nl',
    u'English - Australia': 'en-au',
    u'English - Belize': 'en-bz',
    u'English - Canada': 'en-ca',
    u'English - Caribbean': 'en-cb',
    u'English - Great Britain': 'en-gb',
    u'English - India': 'en-in',
    u'English - Ireland': 'en-ie',
    u'English - Jamaica': 'en-jm',
    u'English - New Zealand': 'en-nz',
    u'English - Phillippines': 'en-ph',
    u'English - Southern Africa': 'en-za',
    u'English - Trinidad': 'en-tt',
    u'English - United States': 'en-us',
    u'Eesti keel': 'et',
    u'føroyskt': 'fo',
    u'فارسی - فارسی': 'fa',
    u'Suomalainen': 'fi',
    u'Français - Belgique': 'fr-be',
    u'Français - Canada': 'fr-ca',
    u'France francaise': 'fr-fr',
    u'Français - Luxembourg': 'fr-lu',
    u'Français - Suisse': 'fr-ch',
    u'БЈР Македонија': 'mk',
    u'Gàidhlig - Èirinn': 'gd-ie',
    u'Gàidhlig - Alba': 'gd',
    u'Deutsch - Österreich': 'de-at',
    u'Deutsches Deutschland': 'de-de',
    u'Deutsch - Liechtenstein': 'de-li',
    u'Deutsch - Luxemburg': 'de-lu',
    u'Deutsch - Schweiz': 'de-ch',
    u'Ελληνικά': 'el',
    u'Guarani - Paraguay': 'gn',
    u'ગુજરાતી': 'gu',
    u'עברית': 'he',
    u'हिंदी': 'hi',
    u'Magyar': 'hu',
    u'Íslensku': 'is',
    u'bahasa Indonesia': 'id',
    u'Italiano - Italia': 'it-it',
    u'Italiano - Svizzera': 'it-ch',
    u'日本人': 'ja',
    u'ಕನ್ನಡ': 'kn',
    u'Kashmiri': 'ks',
    u'Қазақша': 'kk',
    u'ភាសាខ្មែរ': 'km',
    u'한국어': 'ko',
    u'ລາວ': 'lo',
    u'Latine': 'la',
    u'Latviešu': 'lv',
    u'Lietuviškai': 'lt',
    u'Malay - Brunei': 'ms-bn',
    u'Malay - Malaysia': 'ms-my',
    u'മലയാളം': 'ml',
    u'Malti': 'mt',
    u'Maori': 'mi',
    u'मराठी': 'mr',
    u'Монгол хэл': 'mn',
    u'नेपाली': 'ne',
    u'norsk - Bokml': 'no-no',
    u'Norwegian - Nynorsk': 'no-no',
    u'Oriya': 'or',
    u'Polskie': 'pl',
    u'Português - Brasil': 'pt-br',
    u'Português - portugal': 'pt-pt',
    u'ਪੰਜਾਬੀ': 'pa',
    u'Raeto-Romance': 'rm',
    u'Romanian - Moldova': 'ro-mo',
    u'Romanian - Romania': 'ro',
    u'русский': 'ru',
    u'Россия - Молдова': 'ru-mo',
    u'Sanskrit': 'sa',
    u'Сербиан - Цириллиц': 'sr-sp',
    u'Serbian - Latin': 'sr-sp',
    u'Setsuana': 'tn',
    u'سنڌي': 'sd',
    u'සිංහල': 'si',
    u'slovenský': 'sk',
    u'Slovenščina': 'sl',
    u'Somali': 'so',
    u'Sorbian': 'sb',
    u'Español - argentina': 'es-ar',
    u'Español - bolivia': 'es-bo',
    u'Español - chile': 'es-cl',
    u'Español - colombia': 'es-co',
    u'Español - costa rica': 'es-cr',
    u'Español - republica dominicana': 'es-do',
    u'Español - ecuador': 'es-ec',
    u'Español - el salvador': 'es-sv',
    u'Español - guatemala': 'es-gt',
    u'Español - honduras': 'es-hn',
    u'Español - mexico': 'es-mx',
    u'Español - nicaragua': 'es-ni',
    u'Español - panama': 'es-pa',
    u'Español - paraguay': 'es-py',
    u'Español - peru': 'es-pe',
    u'Español - puerto rico': 'es-pr',
    u'Español - españa (tradicional)': 'es-es',
    u'Español - uruguay': 'es-uy',
    u'Español - venezuela': 'es-ve',
    u'Kiswahili': 'sw',
    u'Svenska - finska': 'sv-fi',
    u'Svenska - sverige': 'sv-se',
    u'Тоҷикӣ': 'tg',
    u'தமிழ்': 'ta',
    u'Tatar': 'tt',
    u'తెలుగు': 'te',
    u'ไทย': 'th',
    u'Tibetan': 'bo',
    u'Tsonga': 'ts',
    u'Türk': 'tr',
    u'Turkmen': 'tk',
    u'Українська': 'uk',
    u'اردو': 'ur',
    u'O\'zbekcha - kirillcha': 'uz - uz',
    u'Uzbecorum - Latina': 'uz-uz',
    u'Tiếng Việt': 'vi',
    u'Cymraeg': 'cy',
    u'IsiXhosa': 'xh',
    u'ייִדיש': 'yi',
    u'Zulu': 'zu',
}

LANG_CODE_TO_NAME = dict(
    list((value, key) for key, value in LANG_NAME_TO_CODE.items())
)


class Text(eg.TranslatableStrings):
    Title = "Options"
    Tab1 = "General"
    CheckPreRelease = "Always notify about new pre-releases"
    CheckUpdate = "Check for EventGhost updates at launch"
    confirmDelete = "Confirm deletion of tree items"
    confirmRestart = (
        "Language changes only take effect after restarting the application."
        "\n\n"
        "Do you want to restart EventGhost now?"
    )
    Datestamp = "Datestamp format for log:"
    DatestampHelp = (
        "For imformation on format codes read Python's strftime "
        "documentation:\n"
        "http://docs.python.org/2/library/datetime.html#strftime-and-strptime-"
        "behavior\n"
        "\nHere you can find examples:\n"
        "http://strftime.org/\n"
    )
    HideOnClose = "Keep running in background when window closed"
    HideOnStartup = "Hide on startup"
    LanguageGroup = "Language"
    limitMemory1 = "Limit memory consumption while minimized to"
    limitMemory2 = "MB"
    propResize = "Resize window proportionally"
    refreshEnv = 'Refresh environment before executing "Run" actions'
    showTrayIcon = "Display EventGhost icon in system tray"
    StartWithWindows = 'Autostart EventGhost for user "%s"' % os.environ["USERNAME"]
    UseAutoloadFile = "Autoload file"
    UseFixedFont = 'Use fixed-size font in the "Log" pane'


class OptionsDialog(eg.TaskletDialog):
    instance = None

    @eg.LogItWithReturn
    def Configure(self, parent=None):
        if OptionsDialog.instance:
            OptionsDialog.instance.Raise()
            return
        OptionsDialog.instance = self

        text = Text
        config = eg.config
        self.useFixedFont = config.useFixedFont

        eg.TaskletDialog.__init__(
            self,
            parent=parent,
            title=text.Title,
        )

        languageNames = eg.Translation.languageNames
        languageList = ["en_EN"]
        for item in os.listdir(eg.languagesDir):
            name, ext = os.path.splitext(item)
            if ext == ".py" and name in languageNames:
                languageList.append(name)
        languageList.sort()
        languageNameList = [languageNames[x] for x in languageList]
        notebook = wx.Notebook(self, -1)
        page1 = eg.Panel(notebook)
        notebook.AddPage(page1, text.Tab1)

        # page 1 controls
        startWithWindowsCtrl = page1.CheckBox(
            exists(join((eg.folderPath.Startup or ""), eg.APP_NAME + ".lnk")),
            text.StartWithWindows
        )
        if eg.folderPath.Startup is None:
            startWithWindowsCtrl.Enable(False)

        checkUpdateCtrl = page1.CheckBox(config.checkUpdate, text.CheckUpdate)
        checkPreReleaseCtrl = page1.CheckBox(config.checkPreRelease, text.CheckPreRelease)
        checkPreReleaseCtrl.Enable(config.checkUpdate)

        def OnCheckUpdateCheckBox(event):
            checkPreReleaseCtrl.Enable(event.IsChecked())
        checkUpdateCtrl.Bind(wx.EVT_CHECKBOX, OnCheckUpdateCheckBox)

        confirmDeleteCtrl = page1.CheckBox(
            config.confirmDelete,
            text.confirmDelete
        )

        showTrayIconCtrl = page1.CheckBox(
            config.showTrayIcon,
            text.showTrayIcon
        )

        hideOnCloseCtrl = page1.CheckBox(
            config.hideOnClose,
            text.HideOnClose
        )

        memoryLimitCtrl = page1.CheckBox(config.limitMemory, text.limitMemory1)
        memoryLimitSpinCtrl = page1.SpinIntCtrl(
            config.limitMemorySize,
            min=4,
            max=999
        )

        def OnMemoryLimitCheckBox(dummyEvent):
            memoryLimitSpinCtrl.Enable(memoryLimitCtrl.IsChecked())
        memoryLimitCtrl.Bind(wx.EVT_CHECKBOX, OnMemoryLimitCheckBox)
        OnMemoryLimitCheckBox(None)

        refreshEnvCtrl = page1.CheckBox(
            config.refreshEnv,
            text.refreshEnv
        )

        propResizeCtrl = page1.CheckBox(
            config.propResize,
            text.propResize
        )

        useFixedFontCtrl = page1.CheckBox(
            config.useFixedFont,
            text.UseFixedFont
        )

        def OnFixedFontBox(evt):
            self.UpdateFont(evt.IsChecked())
        useFixedFontCtrl.Bind(wx.EVT_CHECKBOX, OnFixedFontBox)

        datestampCtrl = page1.TextCtrl(config.datestamp)
        datestampCtrl.SetToolTipString(text.DatestampHelp)
        datestampLabel = page1.StaticText(text.Datestamp)
        datestampLabel.SetToolTipString(text.DatestampHelp)
        datestampSzr = wx.BoxSizer(wx.HORIZONTAL)
        datestampSzr.AddMany((
            (datestampLabel, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5),
            (datestampCtrl, 1, wx.EXPAND)
        ))

        def OnDatestampKillFocus(_):
            dt_fmt = datestampCtrl.GetValue()
            try:
                strftime(dt_fmt, localtime())
            except ValueError:
                wx.MessageBox("Invalid format string!", "Error")
                datestampCtrl.SetBackgroundColour("pink")
                datestampCtrl.Refresh()
                wx.CallAfter(datestampCtrl.SetFocus)
            else:
                datestampCtrl.SetBackgroundColour(
                    wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW)
                )
                datestampCtrl.Refresh()

        datestampCtrl.Bind(wx.EVT_KILL_FOCUS, OnDatestampKillFocus)

        languageChoice = BitmapComboBox(page1, style=wx.CB_READONLY)
        for name, code in zip(languageNameList, languageList):
            filename = os.path.join(eg.imagesDir, "flags", "%s.png" % code)
            if os.path.exists(filename):
                image = wx.Image(filename)
                image.Resize((16, 16), (0, 3))
                bmp = image.ConvertToBitmap()
                languageChoice.Append(name, bmp)
            else:
                languageChoice.Append(name)
        languageChoice.SetSelection(languageList.index(config.language))
        languageChoice.SetMinSize((150, -1))

        buttonRow = eg.ButtonRow(self, (wx.ID_OK, wx.ID_CANCEL))

        # construction of the layout with sizers

        flags = wx.ALIGN_CENTER_VERTICAL
        memoryLimitSizer = eg.HBoxSizer(
            (memoryLimitCtrl, 0, flags),
            (memoryLimitSpinCtrl, 0, flags),
            (page1.StaticText(text.limitMemory2), 0, flags | wx.LEFT, 2),
        )

        startGroupSizer = wx.GridSizer(cols=1, vgap=2, hgap=2)
        startGroupSizer.AddMany(
            (
                (startWithWindowsCtrl, 0, flags),
                (checkUpdateCtrl, 0, flags),
                (checkPreReleaseCtrl, 0, flags | wx.LEFT, INDENT_WIDTH),
                (confirmDeleteCtrl, 0, flags),
                (showTrayIconCtrl, 0, flags),
                (hideOnCloseCtrl, 0, flags),
                (memoryLimitSizer, 0, flags),
                (refreshEnvCtrl, 0, flags),
                (propResizeCtrl, 0, flags),
                (useFixedFontCtrl, 0, flags),
                (datestampSzr, 0, flags),
            )
        )

        langGroupSizer = page1.VStaticBoxSizer(
            text.LanguageGroup,
            (languageChoice, 0, wx.LEFT | wx.RIGHT, INDENT_WIDTH),
        )

        page1Sizer = eg.VBoxSizer(
            ((15, 7), 1),
            (startGroupSizer, 0, wx.EXPAND | wx.ALL, 5),
            ((15, 7), 1),
            (langGroupSizer, 0, wx.EXPAND | wx.ALL, 5),
        )
        page1.SetSizer(page1Sizer)
        page1.SetAutoLayout(True)

        sizer = eg.VBoxSizer(
            (notebook, 1, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, 5),
            (buttonRow.sizer, 0, wx.EXPAND),
        )
        self.SetSizerAndFit(sizer)
        self.SetMinSize(self.GetSize())
        notebook.ChangeSelection(0)

        oldLanguage = config.language

        while self.Affirmed():
            config.checkUpdate = checkUpdateCtrl.GetValue()
            config.checkPreRelease = checkPreReleaseCtrl.GetValue()
            config.confirmDelete = confirmDeleteCtrl.GetValue()
            config.showTrayIcon = showTrayIconCtrl.GetValue()
            config.hideOnClose = hideOnCloseCtrl.GetValue()
            config.limitMemory = bool(memoryLimitCtrl.GetValue())
            config.limitMemorySize = memoryLimitSpinCtrl.GetValue()
            config.refreshEnv = refreshEnvCtrl.GetValue()
            config.propResize = propResizeCtrl.GetValue()
            config.useFixedFont = useFixedFontCtrl.GetValue()
            config.datestamp = datestampCtrl.GetValue()
            config.language = languageList[languageChoice.GetSelection()]
            config.Save()
            self.SetResult()

        eg.Utils.UpdateStartupShortcut(startWithWindowsCtrl.GetValue())

        if config.showTrayIcon:
            eg.taskBarIcon.Show()
        else:
            eg.taskBarIcon.Hide()

        if eg.mainFrame:
            eg.mainFrame.SetWindowStyleFlag()
            eg.mainFrame.logCtrl.SetDTLogging()

        if config.language != oldLanguage:
            wx.CallAfter(self.ShowLanguageWarning)

        OptionsDialog.instance = None

    @eg.LogItWithReturn
    def OnCancel(self, event):
        self.UpdateFont(self.useFixedFont)
        self.DispatchEvent(event, wx.ID_CANCEL)

    @eg.LogItWithReturn
    def OnClose(self, event):
        self.UpdateFont(self.useFixedFont)
        self.DispatchEvent(event, wx.ID_CANCEL)

    def ShowLanguageWarning(self):
        dlg = wx.MessageDialog(
            eg.document.frame,
            Text.confirmRestart,
            "",
            wx.YES_NO | wx.ICON_QUESTION
        )
        res = dlg.ShowModal()
        dlg.Destroy()
        if res == wx.ID_YES:
            eg.app.Restart()

    def UpdateFont(self, val):
        font = eg.document.frame.treeCtrl.GetFont()
        if val:
            font = wx.Font(font.GetPointSize(), wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, "Courier New")
        wx.CallAfter(eg.document.frame.logCtrl.SetFont, font)
