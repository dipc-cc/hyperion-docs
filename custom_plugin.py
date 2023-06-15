import os
import shutil
from mkdocs.plugins import BasePlugin


class CustomPlugin(BasePlugin):

    def on_pre_build(self, config):
        # Path to the file you want to modify
        file_path = os.path.join(config['docs_dir'], 'example.md')

        # Modify the file content
        with open(file_path, 'r') as file:
            content = file.read()
            modified_content = content.replace('Hello', 'Hola')

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(modified_content)

        print("Running CustomPlugin...")

    def on_post_build(self, config):
        # Restore the original file content after the build (optional)
        file_path = os.path.join(config['docs_dir'], 'example.md')
        backup_path = os.path.join(config['docs_dir'], 'example_backup.md')

        shutil.move(backup_path, file_path)

        print("CustomPlugin finished.")

