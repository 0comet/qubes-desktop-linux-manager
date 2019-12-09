# Widgets

Available widgets are:
- `qui-domains` - Domains Widget, manages running qubes
- `qui-devices` - Devices Widget, manages attachment/detachment for devices
- `qui-disk-space` - Disk Space Widget, warns about low disk space
- `qui-updates` - Updater Widger, notifies about available updates

## How to run

The widgets should be always available in the widget area of the desktop manager.
They are run (and restarted on crash) by systemd services:
- qubes-widget@qui-domains
- qubes-widget@qui-devices
- qubes-widget@qui-disk-space
- qubes-widget@qui-updates
- qubes-widget@qui-clipboard

In case of problems, you can view system log with `journalctl --user -u qubes-widget@[widget_name]`.

## Translation

To add more translation languages, add a directory in locales with a name corresponding to the target language code, with a subdirectory LC\_MESSAGES in it, copy the file locales/desktop-linux-manager.po into it, and edit its headers to reflect the translation details.

To update base translation files, use the update\_translation.sh script:

`./update_translation.sh`

To test if a translation is working, set the LANG environment variable to desired language and encoding:

`LANG=pl_PL.utf-8 qubes-update-gui`

To push translations to transifex (you will need your own transifex API token):

`tx push --translation`

To update transifex source files:

`tx push --source`

To get translations from transifex:

`tx pull`
