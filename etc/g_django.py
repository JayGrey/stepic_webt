CONFIG = {
        'mode': 'wsgi',
        'user': 'www-data',
        'group': 'www-data',
        'working_dir': '/home/box/web/ask',
        'args': (
            '--bind=0.0.0.0:8000',
            '--workers=1',
            '--timeout=60',
            'wsgi:application',
        ),
}
