"""Voice control of SilverBullet (https://silverbullet.md), a web app, in a web browser.

SilverBullet cannot be told apart from other tabs (its tab titles are just page names), so the commands are active in every browser and
all start with the word "silver". The keys are SilverBullet's defaults (`Mod` is Ctrl on Windows and Linux; the macOS keys differ).
"""
from talon import Module, actions, app, settings

mod = Module()

mod.setting(
    "kolaf_silverbullet_url",
    type=str,
    default="",
    desc='The address of your SilverBullet space, for "silver tab" (for example http://host:3000/notes)',
)


def _palette_run(name: str):
    actions.key("ctrl-/")
    actions.sleep("350ms")
    actions.insert(name)
    actions.sleep("450ms")
    actions.key("enter")


@mod.action_class
class Actions:
    def kolaf_silverbullet_open_page(name: str):
        """Open (or create) a page through SilverBullet's page picker"""
        actions.key("ctrl-k")
        actions.sleep("350ms")
        actions.insert(name)
        actions.sleep("450ms")
        actions.key("enter")

    def kolaf_silverbullet_run(name: str):
        """Run a SilverBullet command by (part of) its name through the command palette"""
        _palette_run(name)

    def kolaf_silverbullet_focus():
        """Switch to the browser tab with SilverBullet, or open it (needs the setting user.kolaf_silverbullet_url and Rango)"""
        url = settings.get("user.kolaf_silverbullet_url")
        if not url:
            app.notify('Set user.kolaf_silverbullet_url (for example in settings.talon) to use "silver tab"')
            return
        try:
            actions.user.rango_focus_or_create_tab_by_url(url)
        except Exception:
            app.notify("Rango is needed for this command; open the SilverBullet tab by hand")
