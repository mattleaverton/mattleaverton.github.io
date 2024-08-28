import re
from pelican import signals

def add_target_blank(content):
    if content._content is not None:
        content._content = re.sub(
            r'(<a\s+(?!.*\btarget=)[^>]*)(href="(?![^"]*{[^"]*})[^"]*")',
            r'\1\2 target="_blank"',
            content._content
        )

def register():
    print('registering blank targeter')
    signals.content_object_init.connect(add_target_blank)
