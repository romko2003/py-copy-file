def copy_file(command: str):
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, src, dst = parts

    if src == dst:
        return

    try:
        with open(src, "rb") as file_in, open(dst, "wb") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
