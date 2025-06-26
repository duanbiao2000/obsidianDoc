import os


def merge_markdown_files(directory, output_file):
    with open(output_file, "w") as outfile:
        for filename in os.listdir(directory):
            if filename.endswith(".md"):
                filepath = os.path.join(directory, filename)
                with open(filepath, "r") as infile:
                    outfile.write(infile.read())
                    outfile.write("\\n---\\n")  # Add a separator between files


if __name__ == "__main__":
    directory = "0. DailyNotes"
    output_file = "0. DailyNotes/combined.md"
    merge_markdown_files(directory, output_file)
