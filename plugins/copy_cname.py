import os
from pelican import signals


def copy_cname(generator):
    output_path = generator.settings['OUTPUT_PATH']
    cname_file = 'CNAME'
    if os.path.exists(cname_file):
        destination = os.path.join(output_path, cname_file)
        os.makedirs(output_path, exist_ok=True)
        with open(cname_file, 'r') as src, open(destination, 'w') as dst:
            dst.write(src.read())


def register():
    signals.finalized.connect(copy_cname)
