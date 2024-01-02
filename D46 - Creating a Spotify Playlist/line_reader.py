def read_specific_line(file_path, line_number):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            if 1 <= line_number <= len(lines):
                return lines[line_number - 1].strip()
            else:
                return f"Error: Line {line_number} does not exist in the file."
    except FileNotFoundError:
        return f"Error: File not found - {file_path}."