
JAZZMIN_SETTINGS = {
    "site_title": "Smart Gate WHS",
    "site_header": "Smart Gate WHS",
    "site_brand": "Smart Gate WHS",
    "site_icon":"./logo.png",
    # Add your own branding here
    # "site_logo": "./logo.png",
    "welcome_sign": "Welcome to the Smart Gate",
    # Copyright on the footer
    "copyright": "Abdulrahman Elsharef",
    "user_avatar": None,
    "language_chooser": False,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
       # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index",
            "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        # {"name": "Support", "url": "https://github.com/AbdulrahmanElsharef",
        #     "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "CONF"},{"app": "WHS"},

        {"name": "STOCK_IN", "url": "https://smartgate.pythonanywhere.com/stock_in/",
            "new_window": True},
        {"name": "STOCK_OUT", "url": "https://smartgate.pythonanywhere.com/stock_out",
            "new_window": True},
        # {"name": "Report", "url": "http://altawheedtech.pythonanywhere.com/report",
        #     "new_window": True},
        # {"name": "Cars", "url": "http://altawheedtech.pythonanywhere.com/cars",
        #     "new_window": True},
        # {"name": "ALtawheed", "url": "https://altawheedgroup.com/",
        #     "new_window": True},
        # {"name": "Check Warranty", "url": "https://warranty.altawheedgroup.com/ar/check/",
        #     "new_window": True},
        # {"name": "WhatsApp", "url": "https://web.whatsapp.com/",
        #     "new_window": True},
        # # {"name": "Messenger", "url": "http://m.me/103844047982053",
        #     "new_window": True},
    ],

    #############
    # User Menu #
    #############
    "order_with_respect_to": ["auth","CRM","Technical","Delvery",],

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/AbdulrahmanElsharef",
            "new_window": True},
        {"model": "auth.user"}
    ],########
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": False,
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "users.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "admin.LogEntry": "fas fa-file",
    },
    # # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-arrow-circle-right",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    # Uncomment this line once you create the bootstrap-dark.css file
    # "custom_css": "css/bootstrap-dark.css",
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,
    ###############
    # Change view #
    ###############
    "changeform_format": "carousel",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "collapsible",
    },
}

JAZZMIN_UI_TWEAKS = {

    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-info",
    "accent": "accent-info",
    "navbar": "navbar-cyan navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-info",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "united",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}
