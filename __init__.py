from anki.hooks import addHook
from . import toneMarks
from . import missingCharacters

addHook('editFocusLost', toneMarks.onFocusLost)
addHook('editFocusLost', missingCharacters.onFocusLost)
