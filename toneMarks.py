from aqt import mw
import re
import functools

sourceField = "发音（拼音）"
destinationField = "声调"

def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

def replace(pattern, replacement):
    return lambda string: re.sub(pattern, replacement, string)

notVowels = r"[^aeiouüAEIOUÜāɑ̄ēīōūǖĀĒĪŌŪǕáɑ́éíóúǘÁÉÍÓÚǗǎɑ̌ěǐǒǔǚǍĚǏǑǓǙàɑ̀èìòùǜÀÈÌÒÙǛ]"

def replaceFifthTone(pinyinString):
    string = pinyinString
    while True:
        newString = re.sub(r"(^|" + notVowels + r"+)[aeiouüAEIOUÜ]+(" + notVowels + r"+|$)", r"˙", string)
        if (newString == string): return string
        string = newString

def getToneCharacters(pinyinString):
    return compose(
        replace(r"[a-zA-Z]*[āɑ̄ēīōūǖĀĒĪŌŪǕ][a-zA-Z]*", r"ˉ"),
        replace(r"[a-zA-Z]*[áɑ́éíóúǘÁÉÍÓÚǗ][a-zA-Z]*", r"ˊ"),
        replace(r"[a-zA-Z]*[ǎɑ̌ěǐǒǔǚǍĚǏǑǓǙ][a-zA-Z]*", r"ˇ"),
        replace(r"[a-zA-Z]*[àɑ̀èìòùǜÀÈÌÒÙǛ][a-zA-Z]*", r"ˋ"),
        replaceFifthTone,
        replace(r"\s", r"")
        )(pinyinString)

def onFocusLost(flag, note, fieldIndex):
    if "普通话" not in note.model()['name']:
        return flag

    sourceIndex = None
    for c, name in enumerate(mw.col.models.fieldNames(note.model())):
        if name == sourceField:
            sourceIndex = c

    if sourceIndex == None:
        return flag

    if fieldIndex != sourceIndex:
        return flag

    if note[destinationField]:
        return flag

    sourceText = mw.col.media.strip(note[sourceField])
    if not sourceText:
        return flag

    note[destinationField] = getToneCharacters(sourceText)
    return True
