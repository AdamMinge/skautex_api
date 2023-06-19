JAZZMIN_SETTINGS = {
    'site_title': 'Skautex Admin',
    'site_header': 'Skautex',
    'welcome_sign': 'Welcome to skautex',
    'user_avatar': None,
    'usermenu_links': [
            {'model': 'accounts.User'}
    ],
    'show_sidebar': True,
    'navigation_expanded': True,
    'hide_apps': [],
    'hide_models': [],
    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
        'accounts.AuditEntry': 'fas fa-user-clock',
        'accounts.User': 'fas fa-user',
        'contact_details.ContactDetail': 'fas fa-address-book',
        'cost_recording.CostRecording': 'fas fa-money-bill-alt',
        'linked_files.LinkedFile': 'fas fa-file',
        'otp_auth.Organization': 'fas fa-building',
        'otp_auth.OrganizationApiKey': 'fas fa-key',
    },
    'default_icon_parents': 'fas fa-chevron-circle-right',
    'default_icon_children': 'fas fa-circle',

    "custom_css": None,
    "custom_js": None,
    "show_ui_builder": False,

    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"accounts.User": "collapsible", "auth.group": "vertical_tabs", },
    "language_chooser": True,
}
