try:
    stream = open(
        r"C:\Users\Ola\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.8\mongo_flask_homework\text\interface.txt",
        "rt", encoding="utf8")
    ch = stream.read(1)
    while ch != '':
        print(ch, end='')
        ch = stream.read(1)
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)