CONFIG = {
        'mode': 'wsgi',
        'user': 'www-data',
        'group': 'www-data',
        'working_dir': '/home/box/web/',
        'args': (
            '--bind=0.0.0.0:8080',
            '--workers=1',
            '--timeout=60',
            'hello:wsgi_app',
        ),
}
