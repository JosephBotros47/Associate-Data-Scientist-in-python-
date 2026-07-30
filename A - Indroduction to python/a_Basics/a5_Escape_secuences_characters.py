# Escape Sequence Characters
# --------------------------
# \b => Back space - remove this character [character]\b
print("Hello\b world") # will remove 'o'

# \n => Line feed character
print("Hello \nworld")

# \r => carriage Return
print("123456\rABcd") # output: ABcd
print("123456\rABcde") # output: ABcde
print("123456\rABcdef") # output: ABcdef
print("123456\rABcdefg") # output: ABcdefg

# \t => Horizontal tab
print("Hello\tworld")

# \x[hexadicimal number] => character hex value
print("\x4F")# output: O
# \newline => Escape new line + \
print("I love \
music and \
sports ")

# \\ => Escape Back Slash
print("I love back slash \\")

# \' => Escape Single Quotes
print("I love single quote \'test\'")

# \" => Escape double Quotes
print("I love single quote \"test\"")