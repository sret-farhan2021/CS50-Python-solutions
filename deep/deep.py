text = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
if(text.strip().lower() == "42" or text.strip().lower() == "forty two" or text.strip().lower() == "forty-two" ):
    print("Yes")
else:
    print("No")
