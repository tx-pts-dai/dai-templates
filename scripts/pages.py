import os

def create_markdown_files(base_dirs):
  for base_dir in base_dirs:
    for dir_ in os.listdir(base_dir):
      if not os.path.isdir(os.path.join(base_dir, dir_)):
        continue
      template_dir = os.path.join(base_dir, dir_)
      if 'README.md' in os.listdir(template_dir):
        markdown_content = f'{{% include "../../{template_dir}/README.md" %}}\n'
        markdown_file_path = os.path.join("docs/templates_", f"{dir_}.md")
        with open(markdown_file_path, 'w') as f:
          f.write(markdown_content)


if __name__ == "__main__":
  base_dirs = ["addons", "bases"]
  create_markdown_files(base_dirs)