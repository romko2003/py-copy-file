def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, source_filename, target_filename = parts

    if source_filename == target_filename:
        return

    try:
        with (open(source_filename, "rb") as file_in,
              open(target_filename, "wb") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
