#!/bin/bash

CONTENT_DIR="$1"
ARTICLE_NAME="$2"

# Add .md extension if not present
[[ "$ARTICLE_NAME" != *.md ]] && ARTICLE_NAME="${ARTICLE_NAME}.md"

# Find the file
ARTICLE_PATH=$(find "$CONTENT_DIR" -type f -name "*${ARTICLE_NAME}*" | head -n 1)

if [ -z "$ARTICLE_PATH" ]; then
    echo "Could not find article matching: $ARTICLE_NAME"
    exit 1
fi

# Start the Python editor server
python3 util/editor_server.py "$ARTICLE_PATH"
