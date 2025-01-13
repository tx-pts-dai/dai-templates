import os
from dotenv import load_dotenv
import openai

def read_file_content(file_path):
    """Read file content, skipping if there's an error."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception:
        return "[Could not read file content]"

def process_directory_files(directory):
    """Process all files in a directory and return their contents."""
    files_content = ""

    for root, dirs, files in os.walk(directory):
        # Skip hidden files and directories
        # dirs[:] = [d for d in dirs if not d.startswith('.')]
        # files = [f for f in files if not f.startswith('.')]

        for filename in files:
            file_path = os.path.join(root, filename)
            relative_path = os.path.relpath(file_path, directory)
            content = read_file_content(file_path)
            files_content += f"\n# {relative_path}\n{content}\n"

    return files_content

def generate_docs(files_content):
    """Generate documentation using OpenAI API."""
    prompt = f"""
        Write a readme file that documents the contents of this directory.
        Include descriptions of the files and their purposes.

        Directory contents:
        {files_content}
    """

    openai_api = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    response = openai_api.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-4o-mini",
    )
    return response.choices[0].message.content

def create_markdown_files(base_dir):
    """Create README.md files for each directory."""
    if not os.path.exists(base_dir):
        print(f"Warning: Directory {base_dir} does not exist")
        return

    for root, dirs, _ in os.walk(base_dir):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        readme_path = os.path.join(root, "README.md")
        if os.path.exists(readme_path):
            print(f"Skipping {root} - README.md already exists")
            continue

        print(f"Processing {root}")
        files_content = process_directory_files(root)

        if files_content:
            docs = generate_docs(files_content)
            with open(readme_path, "w", encoding='utf-8') as file:
                file.write(docs)
            print(f"Created README.md in {root}")

def main():
    """Main function to run the documentation generator."""
    load_dotenv()

    if not os.getenv('OPENAI_API_KEY'):
        raise ValueError("OPENAI_API_KEY environment variable is not set")

    folder_path = "bases/"
    create_markdown_files(folder_path)

if __name__ == "__main__":
    main()