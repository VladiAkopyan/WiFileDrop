from CTkMessagebox import CTkMessagebox

def message_error(_title, _message):
    CTkMessagebox(title=_title, message=_message, icon='error')

def message_warning(_title, _message):
    CTkMessagebox(title=_title, message=_message, icon='warning')

def message_success(_title, _message):
    CTkMessagebox(title=_title, message=_message, icon='check')