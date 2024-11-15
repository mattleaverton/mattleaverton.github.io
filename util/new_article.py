import sys
import os
import subprocess
from datetime import datetime

def create_article(content_dir, name):
    # Convert name to filename format
    filename = name.lower().replace(' ', '-')
    if not filename.endswith('.md'):
        filename += '.md'

    filepath = os.path.join(content_dir, 'writing', filename)

    # Create article template
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    template = f"""Title: {name}
Date: {now}
Modified: {now}
Category: Writing
Tags:
Slug: {filename[:-3]}  # Remove .md extension
Authors: Matt Leaverton
Summary:
Status: draft

"""

    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Write the file
    with open(filepath, 'w') as f:
        f.write(template)

    # Open in editor - use shell=True to access shell environment
    subprocess.run('cursor "{}"'.format(filepath), shell=True)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: new_article.py <content_dir> <article name>")
        sys.exit(1)
    create_article(sys.argv[1], sys.argv[2])
