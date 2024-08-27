import os
from pelican import signals


def remove_original_images(generator):
    output_path = generator.settings['OUTPUT_PATH']
    static_paths = generator.settings.get('STATIC_PATHS', [])

    for static_path in static_paths:
        static_dir = os.path.join(output_path, static_path)
        if os.path.exists(static_dir):
            for root, dirs, files in os.walk(static_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    if 'derivatives' not in file_path:
                        os.remove(file_path)

def register():
    signals.finalized.connect(remove_original_images)
