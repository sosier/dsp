from advanced_python_regex import emailList

file_name = "python/emails.csv"
f = open(file_name, "w")
f.write("\n".join(emailList))
f.close()
