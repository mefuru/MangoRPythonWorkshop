
path2script='"C:/path/to my/script.py"'

args = c("arg1", "y", "5", "1231244")  # Variable number of args in a vector

cmd = paste("python", path2script, paste(args, collapse=" "))

system(cmd)