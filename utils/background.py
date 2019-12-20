import os
import platform


def change_background(file_path):
    if platform.system().lower().startswith('win'):
        # import windows specific modules and execute
        pass
    elif platform.system().lower().startswith('lin'):
        # import linux specific modules and execute
        import subprocess
        return change_linux_background(file_path)
    elif platform.system().lower().startswith('dar'):
        # import mac OS specific modules and execute
        pass


def change_linux_background(file_path):
    """
    Change the background on linux operating systems
    """
    # Initialize variables
    ARG_MAP = {
        'feh': ['feh', ['--bg-center'], '%s'],
        'gnome': [
            'gsettings',
            ['set', 'org.gnome.desktop.background', 'picture-uri'], 'file://%s'
        ]
    }

    WM_BKG_SETTERS = {
        'spectrwm': ARG_MAP['feh'],
        'scrotwm': ARG_MAP['feh'],
        'wmii': ARG_MAP['feh'],
        'i3': ARG_MAP['feh'],
        'awesome': ARG_MAP['feh'],
        'awesome-gnome': ARG_MAP['gnome'],
        'gnome': ARG_MAP['gnome'],
        'ubuntu': ARG_MAP['gnome']
    }

    # Try to find background setter
    desktop_environ = os.environ.get('DESKTOP_SESSION', '')

    # Get settings arguments
    if desktop_environ and desktop_environ in WM_BKG_SETTERS:
        bkg_setter, args, pic_arg = WM_BKG_SETTERS.get(desktop_environ,
                                                       [None, None])
    else:
        bkg_setter, args, pic_arg = WM_BKG_SETTERS['spectrwm']

    # Parse and execute background change command
    pargs = [bkg_setter] + args + [pic_arg % file_path]
    subprocess.call(pargs)
