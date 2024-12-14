def function_with_unclosed_file(filename):
    try:
        f = open(filename, 'r')
        # Some operations on the file
        # ...
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    # Missing f.close()
    return