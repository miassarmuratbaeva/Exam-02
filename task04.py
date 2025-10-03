def format_name(full_name: str) -> str:
    a = full_name.split()
    return f"{a[1]} {a[2]},{a[0]}"
print(format_name("Aliyev Vali G'aniyevich"))