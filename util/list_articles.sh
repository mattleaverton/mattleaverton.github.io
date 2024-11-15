#!/bin/bash

CONTENT_DIR="$1"
CATEGORY="${2:-writing}"  # Default to 'writing' if no category specified

if [ -d "$CONTENT_DIR/$CATEGORY" ]; then
    find "$CONTENT_DIR/$CATEGORY" -name "*.md" -type f | sed "s|$CONTENT_DIR/||" | less
else
    echo "Category '$CATEGORY' not found"
    exit 1
fi
