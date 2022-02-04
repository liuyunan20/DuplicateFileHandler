import re
# its first part can contain from 6 to 30 characters.
# These characters can be lowercase Latin letters, digits, hyphens -,
# the dot characters . , the equals sign = or underscores _
# the second part that immediately follows the first one is always @hyperskill.org

template = r'[a-z0-9-\.=_]{6,30}@hyperskill\.org'
