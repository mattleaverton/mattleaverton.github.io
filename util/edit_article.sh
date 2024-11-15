#!/bin/bash

CONTENT_DIR="$1"
ARTICLE_NAME="$2"

# Add .md extension if not present
[[ "$ARTICLE_NAME" != *.md ]] && ARTICLE_NAME="${ARTICLE_NAME}.md"

# Find the file (with basic fuzzy matching)
ARTICLE_PATH=$(find "$CONTENT_DIR" -type f -name "*${ARTICLE_NAME}*" | head -n 1)

if [ -z "$ARTICLE_PATH" ]; then
    echo "Could not find article matching: $ARTICLE_NAME"
    exit 1
fi

# Update modified date using Python
python - "$ARTICLE_PATH" <<EOF
import sys
from datetime import datetime
import re

filepath = sys.argv[1]
with open(filepath, 'r') as f:
    content = f.read()

now = datetime.now().strftime("%Y-%m-%d %H:%M")
modified_line = f"Modified: {now}\n"

if 'Modified:' in content:
    content = re.sub(r'Modified:.*\n', modified_line, content)
else:
    content = re.sub(r'(Title:.*\n)', f'\\1{modified_line}', content)

with open(filepath, 'w') as f:
    f.write(content)
EOF

# Open in editor
~/Applications/$(ls ~/Applications | grep -o 'cursor.*\.AppImage$') -r --no-sandbox --disable-gpu-sandbox "$ARTICLE_PATH" 2>/dev/null
