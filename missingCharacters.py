from aqt import mw

sourceField = "单词（用汉字）"
destinationFields = [
    "第一个字单词填空",
    "第二个字单词填空",
    "第三个字单词填空",
    "第四个字单词填空",
    ]

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


    sourceText = mw.col.media.strip(note[sourceField])
    if not sourceText:
        return flag

    for i in range(0, min(len(sourceText), len(destinationFields))):
        if not note[destinationFields[i]]:
            note[destinationFields[i]] = sourceText[:i] + "__" + sourceText[i + 1:]
            flag = True

    return flag
