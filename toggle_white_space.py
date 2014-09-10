import sublime
import sublime_plugin

class ToggleWhiteSpaceCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		settings = sublime.load_settings("Preferences.sublime-settings")
		if settings.get("draw_white_space") != "all":
			settings.set("draw_white_space", "all")
		else:
			settings.erase("draw_white_space")
		sublime.save_settings("Preferences.sublime-settings")