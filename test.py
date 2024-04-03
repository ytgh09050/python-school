with open("作業.txt", "r") as f:
    # 列印前30個字元
    print(f.read(30))
    # 重新將檔指標移到檔頭部
    f.seek(0)
    # 列印前3行內容
    for i in range(3):
        print(f.readline().strip())
