#single line string
name='prasad'
print(name)

#dubble line string
greeting="hello world"
print(greeting)

#multi line string
info="""this is first line .
this is a second line."""
print(info)
print("---------------------------------------")


#built-in function of string

#len()--------------------------
Msg="hello python"
print(len(Msg))

#uppercase()----------------------
Msg="hello python"
print(Msg.upper())

#lowercase----------------------
msg="HELLO PYTHON"
print(msg.lower())

#title--------------------------
msg="hello python world"
print(msg.title())

#strip--------------------------
msg="             hello python world "
print(msg.strip())
msg="                 hello python world "
print(msg)

#find-----------------------------
msg="i was learn a python"
print(msg.find("python"))

#replace-------------------------------
msg="i like java"
print(msg.replace("java","python"))

#split- string convert to tuple-------
msg="apple,mango,banana"
print(msg.split(","))

#count------------------------------------
msg="i like python"
print(msg.count("i"))

#startwith----------------------------
msg="i like python"
print(msg.startswith("i"))
print(msg.endswith("n"))
print("------------------------------------")


#string operator------------------------

#concatition
a="hello"
b="world"
result=a + b
print(result.upper())

#repetition
msg="hi!"
print(msg*3,sep="-")
print("---------------------------------")

#string slicing -----------------------------------
msg="python"
print(msg[0:4])
print(msg[:3])
print(msg[3:])
print(msg[::-1])
ans="abcdef"
print(ans[::2])
#-----------------------------
s="python"
result=s[0:6:2]
print(result)



a=1+2
print(a)
age=20
print(type(age))
name="prasad"
age=19
print(name,age)
#1-concatenation
''' a=1+"2"
 print(a)'''

#2-len
name="prasad"
print(len(name))
