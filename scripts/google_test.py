import os
from dotenv import load_dotenv
import google.generativeai as genai


def chat(input):
    # Create the model
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 40,
      "max_output_tokens": 8192,
      "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
      model_name="gemini-1.5-flash-8b",
      generation_config=generation_config,
      system_instruction="Review all the input code and generate a detailed readme.md explaining the use of the code and how to use it. be creative and invent your own opinions as well to what should be included in the docs. ",
    )

    chat_session = model.start_chat(
      history=[
      ]
    )

    response = chat_session.send_message(input)

    return response.text

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
        for filename in files:
            file_path = os.path.join(root, filename)
            relative_path = os.path.relpath(file_path, directory)
            content = read_file_content(file_path)
            files_content += f"\n# {relative_path}\n{content}\n"

    return files_content

def create_file(file_path, content):
    """Create a file with the given content."""
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error creating file {file_path}: {e}")


def main():
    """Main function to run the documentation generator."""
    load_dotenv()


    base_path = "addons"

    for folder in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder)
        if not os.path.isdir(folder_path):
            continue
        data = process_directory_files(folder_path)
        readme_content = chat(data)
        create_file(os.path.join(folder_path, "README.md"), readme_content)

    # create_markdown_files(folder_path)

if __name__ == "__main__":
    main()