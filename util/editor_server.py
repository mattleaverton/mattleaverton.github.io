import http.server
import socketserver
import webbrowser
import json
import os
import sys
import shutil
from pathlib import Path

class EditorHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('util/editor.html', 'rb') as f:
                self.wfile.write(f.read())
        elif self.path == '/article':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            with open(os.environ['ARTICLE_PATH'], 'r') as f:
                content = f.read()
            self.wfile.write(json.dumps({'content': content}).encode())

    def do_POST(self):
        if self.path == '/save':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            article_data = json.loads(post_data)

            # Save the article content
            with open(os.environ['ARTICLE_PATH'], 'w') as f:
                f.write(article_data['content'])

            # Handle image paths if present
            if 'images' in article_data and article_data['images']:
                images_dir = Path('content/images')
                images_dir.mkdir(parents=True, exist_ok=True)

                print(article_data['images'])
                for image_path in article_data['images']:
                    # Get the source image path
                    src_path = Path(image_path)
                    if not src_path.exists():
                        print(f"Warning: Image not found at {src_path}")
                        continue

                    # Copy to destination
                    dest_path = images_dir / src_path.name
                    shutil.copy2(src_path, dest_path)
                    print(f"Copied image from {src_path} to {dest_path}")

            self.send_response(200)
            self.end_headers()
            raise Exception('done')

def main():
    if len(sys.argv) != 2:
        print("Usage: python editor_server.py <article_path>")
        sys.exit(1)

    article_path = sys.argv[1]
    os.environ['ARTICLE_PATH'] = article_path

    PORT = 8000
    Handler = EditorHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Editor server started at http://localhost:{PORT}")
        webbrowser.open(f'http://localhost:{PORT}')
        try:
            httpd.serve_forever()
        except (Exception, KeyboardInterrupt):
            print("\nShutting down server...")
            httpd.shutdown()

if __name__ == "__main__":
    main()
