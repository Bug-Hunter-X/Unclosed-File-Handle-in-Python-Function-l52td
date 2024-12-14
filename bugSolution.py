def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # Some operations on the file
            # ...
            for line in f:
                # process each line
                print(line)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return