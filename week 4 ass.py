import os

def read_and_modify_file(input_filename, output_filename, modification_func):
    """
    Reads content from an input file, applies a modification, and writes
    the modified content to an output file. Handles common file-related errors.

    Args:
        input_filename (str): The name of the file to read from.
        output_filename (str): The name of the file to write the modified content to.
        modification_func (function): A function that takes a string (line from input)
                                      and returns a modified string.
    """
    try:
        # Step 1: Read from the input file
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
        print(f"Successfully read from '{input_filename}'.")

        # Step 2: Modify the content
        modified_lines = [modification_func(line) for line in lines]
        print("Content successfully modified.")

        # Step 3: Write to the output file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)
        print(f"Successfully wrote modified content to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found. Please check the filename and try again.")
    except IOError as e:
        print(f"Error: Could not read or write file. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- Example Modification Function ---
def capitalize_and_add_prefix(line):
    """
    Example modification: Capitalizes the line and adds a prefix.
    """
    return f"MODIFIED: {line.strip().upper()}\n"

# --- Main part of the program ---
if __name__ == "__main__":
    print("Welcome to the File Processor! 🖋️")
    print("This program reads a file, modifies its content, and writes to a new file.")
    print("It also includes error handling for common file operations.")

    # Get input filename from the user
    while True:
        user_input_filename = input("\nEnter the name of the input file (e.g., 'my_story.txt'): ")
        # Basic check if the file exists before attempting to read
        if not os.path.exists(user_input_filename):
            print(f"Warning: '{user_input_filename}' does not exist. Please make sure the file is in the same directory.")
            continue # Ask again for the input file
        break # Exit loop if file exists or user wants to proceed anyway

    # Get output filename from the user
    user_output_filename = input("Enter the name for the output file (e.g., 'modified_story.txt'): ")

    # Run the file processing with the example modification function
    read_and_modify_file(user_input_filename, user_output_filename, capitalize_and_add_prefix)

    print("\nFile processing complete! 🎉")
    print(f"Check '{user_output_filename}' for the modified content.")

