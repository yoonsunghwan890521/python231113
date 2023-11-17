#파일 쓰기
f = open("c:\\work2\\test.txt", "wt", encoding="utf-8")
f.write("첫번째라인\n두번째라인\n세번째라인\n")
f.close()

#파일에 첨부 (append, read, write)
f = open("c:\\work2\\test.txt", "a+", encoding="utf-8")
f.write("추가로 첨부하기\n")
f.close()

#파일 읽기
f = open("c:\\work2\\test.txt", "rt", encoding="utf-8")
print(f.read())
f.close()


#서식 지정
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(100000))
print("{0:e}".format(1/3))
print("{0:f}".format(1/3))
print("{0:2f}".format(1/3))
