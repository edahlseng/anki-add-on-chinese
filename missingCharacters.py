from aqt import mw

sourceField = "Word (in Hanzi)"
destinationFields = [
    "First Character Blanked Out (if multiple characters & vocab card)",
    "Second Character Blanked Out (if multiple characters & vocab card)",
    "Third Character Blanked Out (if multiple characters & vocab card)",
    "Fourth Character Blanked Out (if multiple characters & vocab card)",
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
