def count_lines(path):
    """读取文件并统计行数，文件不存在时友好提示"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        print(f"文件 {path} 共 {len(lines)} 行：")
        for i, line in enumerate(lines, 1):
            print(f"{i}. {line.rstrip()}")
        return len(lines)
    except FileNotFoundError:
        print(f"⚠️ 找不到文件：{path}")
        return 0

if __name__ == "__&#8203;main__":
    count_lines("todo.txt")
