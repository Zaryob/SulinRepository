#!/usr/bin/python
# -*- coding: utf-8 -*-

# Mudur configuration open

CONF = "/etc/conf.d/scomd"
TTY_DEFAULT = 6
LANGUAGES = {
    "tr":   Language(
        name                = _("Turkish"),
        locale              = "tr_TR.UTF-8",
        console_font        = "lat5u-16",
        console_translation = "8859-9",
        keymaps             = [
            Keymap("trq", "tr", name = _("Turkish Q")),
            Keymap("trf", "tr", "f", _("Turkish F"))
        ]
    ),

    "en":   Language(
        name                = _("English"),
        locale              = "en_US.UTF-8"
    ),

    "en_GB":    Language(
        name                = _("English GB"),
        locale              = "en_GB.UTF-8",
        keymaps             = [Keymap("uk", "gb")]
    ),

    "af":   Language(
        name                = _("Afrikaans"),
        locale              = "af_ZA.UTF-8",
        keymaps             = [Keymap("us")]
    ),

    "ar":   Language(
        name                = _("Arabic"),
        locale              = "ar_SA.UTF-8",
        keymaps             = [Keymap("us", "ara")]
    ),

    "be":   Language(
        name                = _("Belgium"),
        locale              = "be_BY.UTF-8",
        keymaps             = [Keymap("be-latin1", "be")]
    ),

    "bg":   Language(
        name                = _("Bulgarian"),
        locale              = "bg_BG.UTF-8",
        keymaps             = [Keymap("bg")]
    ),

    "ca":   Language(
        name                = _("Catalan"),
        locale              = "ca_ES.UTF-8",
        keymaps             = [Keymap("es")]
    ),

    "cy":   Language(
        name                = _("Welsh"),
        locale              = "cy_GB.UTF-8",
        keymaps             = [Keymap("uk", "gb")]
    ),

    "cz":   Language(
        name                = _("Czech"),
        locale              = "cs_CZ.UTF-8",
        keymaps             = [Keymap("cz-lat2", "cz")]
    ),

    "da":   Language(
        name                = _("Danish"),
        locale              = "da_DK.UTF-8",
        keymaps             = [Keymap("dk")]
    ),

    "de":   Language(
        name                = _("German"),
        locale              = "de_DE.UTF-8",
        keymaps             = [Keymap("de-latin1-nodeadkeys", "de")]
    ),

    "es":   Language(
        name                = _("Spanish"),
        locale              = "es_ES.UTF-8",
        keymaps             = [Keymap("es")]
    ),

    "et":   Language(
        name                = _("Estonian"),
        locale              = "et_EE.UTF-8",
        keymaps             = [Keymap("et", "ee")]
    ),

    "fi":   Language(
        name                = _("Finnish"),
        locale              = "fi_FI.UTF-8",
        keymaps             = [Keymap("fi")]
    ),

    "fr":   Language(
        name                = _("French"),
        locale              = "fr_FR.UTF-8",
        keymaps             = [Keymap("fr-latin1", "fr")]
    ),

    "gr":   Language(
        name                = _("Greek"),
        locale              = "el_GR.UTF-8",
        keymaps             = [Keymap("gr")]
    ),

    "hr":   Language(
        name                = _("Croatian"),
        locale              = "hr_HR.UTF-8",
        keymaps             = [Keymap("croat", "hr")]
    ),

    "hu":   Language(
        name                = _("Hungarian"),
        locale              = "hu_HU.UTF-8",
        console_font        = "lat2a-16",
        console_translation = "8859-2",
        keymaps             = [Keymap("hu")]
    ),

    "is":   Language(
        name                = _("Icelandic"),
        locale              = "is_IS.UTF-8",
        keymaps             = [Keymap("is-latin1", "is")]
    ),

    "it":   Language(
        name                = _("Italian"),
        locale              = "it_IT.UTF-8",
        keymaps             = [Keymap("it")]
    ),

    "ja":   Language(
        name                = _("Japanese"),
        locale              = "ja_JP.UTF-8",
        keymaps             = [Keymap("jp106", "jp")]
    ),

    "mk":   Language(
        name                = _("Macedonian"),
        locale              = "mk_MK.UTF-8",
        keymaps             = [Keymap("mk")]
    ),

    "ml":   Language(
        name                = _("Malayalam"),
        locale              = "ml_IN.UTF-8",
        keymaps             = [Keymap("us")]
    ),

    "nb":   Language(
        name                = _("Norwegian"),
        locale              = "nb_NO.UTF-8",
        keymaps             = [Keymap("no")]
    ),

    "nl":   Language(
        name                = _("Dutch"),
        locale              = "nl_NL.UTF-8",
        keymaps             = [Keymap("us")]
    ),

    "pl":   Language(
        name                = _("Polish"),
        locale              = "pl_PL.UTF-8",
        keymaps             = [Keymap("pl2", "pl")]
    ),

    "pt":   Language(
        name                = _("Portuguese"),
        locale              = "pt_PT.UTF-8",
        keymaps             = [Keymap("pt-latin1", "pt")]
    ),

    "pt_BR":   Language(
        name                = _("Brazilian"),
        locale              = "pt_BR.UTF-8",
        keymaps             = [Keymap("br-abnt2", "br")]
    ),

    "ru":   Language(
        name                = _("Russian"),
        locale              = "ru_RU.UTF-8",
        console_font        = "Cyr_a8x16",
        console_translation = "8859-5",
        keymaps             = [Keymap("ru")]
    ),

    "sk":   Language(
        name                = _("Slovak"),
        locale              = "sk_SK.UTF-8",
        keymaps             = [Keymap("sk-qwerty", "sk")]
    ),

    "sl":   Language(
        name                = _("Slovenian"),
        locale              = "sl_SI.UTF-8",
        keymaps             = [Keymap("slovene", "si")]
    ),

    "sr":   Language(
        name                = _("Serbian"),
        locale              = "sr_CS.UTF-8",
        keymaps             = [Keymap("sr-cy", "rs")]
    ),

    "sv":   Language(
        name                = _("Swedish"),
        locale              = "sv_SE.UTF-8",
        console_font        = "lat0-16",
        keymaps             = [Keymap("sv-latin1", "se")]
    ),

    "uk":   Language(
        name                = _("Ukrainian"),
        locale              = "uk_UA.UTF-8",
        keymaps             = [Keymap("ua-utf", "ua")]
    ),

    "vi":   Language(
        name                = _("Vietnamese"),
        locale              = "vi_VN.UTF-8",
        keymaps             = [Keymap("us", "vn")]
    )
}
# Required utils

def getConf(key, default=None):
    value = default
    for line in open(CONF):
        line = line.strip()
        try:
            _key, _value = line.split("=", 1)
        except ValueError:
            continue
        _key = _key.strip()
        if key == _key:
            value = _value.strip()
            if value.startswith('"') or value.startswith("'"):
                value = value[1:-1]
            break
    return value

def setConf(key, value=None):
    data = open(CONF).read()
    lines = data.split("\n")
    for index, line in enumerate(lines):
        try:
            _key, _value = line.split("=", 1)
        except ValueError:
            continue
        _key = _key.strip()
        if key == _key or (_key.startswith("#") and _key[1:].strip() == key):
            if value:
                lines[index] = "%s = '%s'" % (key, value)
            elif not line.startswith("#"):
                lines[index] = "# %s" % line
    open(CONF, "w").write("\n".join(lines))

# System.Settings methods

def listLanguages():
    languages = []
    for code, info in LANGUAGES.iteritems():
        languages.append((code, str(info.name)))
    return languages

def getLanguage():
    return getConf("language", "en")

def setLanguage(lang):
    if not len(lang):
        lang = None
    setConf("language", lang)


def listKeymaps(language):
    keymaps = []
    if language and language in LANGUAGES:
        for keymap in LANGUAGES[language].keymaps:
            keymaps.append((keymap.console_layout, str(keymap.name)))
    else:
        for language in LANGUAGES:
            for keymap in LANGUAGES[language].keymaps:
                keymaps.append((keymap.console_layout, str(keymap.name)))
    return keymaps

def getKeymap():
    return getConf("keymap", "us")

def setKeymap(keymap):
    if not len(keymap):
        keymap = None
    setConf("keymap", keymap)


def getHeadStart():
    return getConf("head_start")

def setHeadStart(package):
    if not len(package):
        package = None
    setConf("head_start", package)


def getClock():
    is_utc = getConf("clock", "local") == "UTC"
    adjust = getConf("clock_adjust", "no") == "yes"
    return is_utc, adjust

def setClock(is_utc, adjust):
    if is_utc:
        setConf("clock", "UTC")
    else:
        setConf("clock", "local")
    if adjust:
        setConf("clock_adjust", "yes")
    else:
        setConf("clock_adjust", "no")


def getTTYs():
    count = getConf("tty_number", TTY_DEFAULT)
    try:
        return int(count)
    except (ValueError, TypeError):
        return TypeError

def setTTYs(count):
    setConf("tty_number", count)
