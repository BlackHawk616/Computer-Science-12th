# Writing a python function to  merge the contents of two text files into third file
def merge_files(file1, file2, output_file):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2, open(output_file, 'w', encoding='utf-8') as out:
        out.write(f1.read())  # Read and write contents of first file
        out.write("\n")  # Add a new line for separation
        out.write(f2.read())  # Read and write contents of second file
    
    print(f"Contents of {file1} and {file2} merged into {output_file} successfully!")

# Example usage
merge_files("file1.txt", "file2.txt", "merged.txt")
