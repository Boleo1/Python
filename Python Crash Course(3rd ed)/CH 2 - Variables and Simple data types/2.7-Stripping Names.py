# This program shows off the .strip .lstrip and .rstrip operands and how they work, also notice how that the white space in the middle of the word is still there.

right_space = "anthony   "
left_space = "   anthony"
space = "  ant  hony  "

print(right_space.rstrip())
print(left_space.lstrip())
print(space.strip())