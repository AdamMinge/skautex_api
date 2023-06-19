SWAGGER_SETTINGS = {
    'DEFAULT_AUTO_SCHEMA_CLASS': 'core.swagger_auto_schema.PermissionsAutoSchema',
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Api-Key'
        },
        'auth_token': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
}

REDOC_SETTINGS = {
   'LAZY_RENDERING': False,
}
