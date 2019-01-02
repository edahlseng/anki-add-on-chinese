from anki.hooks import addHook
from . import toneMarks
from . import missingCharacters
from . import exampleSentence

addHook('editFocusLost', toneMarks.onFocusLost)
addHook('editFocusLost', missingCharacters.onFocusLost)
addHook('editFocusLost', exampleSentence.onFocusLost)
