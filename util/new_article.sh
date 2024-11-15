#!/bin/bash

CONTENT_DIR="$1"
ARTICLE_NAME="$2"

# Convert name to filename format
FILENAME=$(echo "$ARTICLE_NAME" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
[[ "$FILENAME" != *.md ]] && FILENAME="${FILENAME}.md"

FILEPATH="$CONTENT_DIR/writing/$FILENAME"

# Create directory if it doesn't exist
mkdir -p "$(dirname "$FILEPATH")"

if [ -f "$FILEPATH" ]; then
    echo "Article already exists"
else
    # Create article template using Python (for consistent datetime handling)
    python - "$ARTICLE_NAME" "$FILEPATH" <<EOF
from datetime import datetime
import sys

name, filepath = sys.argv[1:]
now = datetime.now().strftime("%Y-%m-%d %H:%M")
template = f"""Title: {name}
Modified: {now}
Date: {now}
Category: Writing
Tags:
Slug:
Authors: Matt Leaverton
Summary:
Status: draft

"""

with open(filepath, 'w') as f:
    f.write(template)
EOF
fi

# Open in editor
~/Applications/$(ls ~/Applications | grep -o 'cursor.*\.AppImage$') -r --no-sandbox --disable-gpu-sandbox "$FILEPATH" 2>/dev/null
