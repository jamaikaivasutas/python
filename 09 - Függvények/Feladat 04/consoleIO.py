def message(name) -> str:
    size = len(name)
    message = fg(size) + name + fg.rs
    return message