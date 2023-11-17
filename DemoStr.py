# Demo Str.py

strA = "python is very powerful"
strB = "파이썬은 강력해"
print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("p"))
print(strA.startswith("py"))
print(strA.endswith("py"))

print("-----알파벳 숫자 구성확인------")
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

data = "<<< spam and ham >>>"
result = data.strip("<> ")
print(data)
print(result)
result = result.replace("spam","spam egg")
print("변환결과")
print(result)
lst = result.split()
print(lst)
print(" ".join(lst))

