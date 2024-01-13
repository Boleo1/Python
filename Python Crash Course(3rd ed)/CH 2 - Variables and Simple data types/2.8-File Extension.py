# This program shows off .removeprefix and .removesuffix

url = "https://www.github.com/boleo1"
simpleurl = url.removeprefix("https://www.")
print(simpleurl)

filename = "code/python_files.txt"
simplefile = filename.removesuffix(".txt")
print(simplefile)