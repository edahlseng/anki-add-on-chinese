from aqt import mw
from aqt.utils import showInfo

wordSourceField = "单词（用汉字）"
sentenceSourceField = "完整句子"
destinationField = "句子填空"

def onFocusLost(flag, note, fieldIndex):
    if "普通话" not in note.model()['name']:
        return flag

    # Get sentence

    sentenceSourceIndex = None
    for c, name in enumerate(mw.col.models.fieldNames(note.model())):
        if name == sentenceSourceField:
            sentenceSourceIndex = c

    if sentenceSourceIndex == None:
        return flag

    if fieldIndex != sentenceSourceIndex:
        return flag

    sentenceSourceText = mw.col.media.strip(note[sentenceSourceField])
    if not sentenceSourceText:
        return flag

    # Get word

    wordSourceIndex = None
    for c, name in enumerate(mw.col.models.fieldNames(note.model())):
        if name == wordSourceField:
            wordSourceIndex = c

    if wordSourceIndex == None:
        return flag

    wordSourceText = mw.col.media.strip(note[wordSourceField])
    if not wordSourceText:
        return flag

    # Update destination field

    if not note[destinationField]:
        note[destinationField] = sentenceSourceText.replace(wordSourceText, "__")
        flag = True

    return flag
