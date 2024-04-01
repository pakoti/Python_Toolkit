def remove_comments(input_file_path, output_file_path):
    """
    Removes comments from a Python file and saves the cleaned content to a new file.
    """
    cleaned_lines = []
    with open(input_file_path, "r") as file:
        for line in file:
            # Skip lines starting with '#'
            if not line.strip().startswith("#"):
                cleaned_lines.append(line)

    # Write cleaned content to a new file
    with open(output_file_path, "w") as output_file:
        output_file.writelines(cleaned_lines)

if __name__ == "__main__":
    input_file_path = "//path" 
    output_file_path = "//path"
    remove_comments(input_file_path, output_file_path)
    print(f"Comments removed and saved to {output_file_path}")

