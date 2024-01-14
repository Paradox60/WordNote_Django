"""
An app that does lots of stuff
"""

# code taken from https://github.com/beeware/toga/tree/main/examples/positron-django

import os
import socketserver
from threading import Event, Thread
from wsgiref.simple_server import WSGIServer

import django
from django.core.handlers.wsgi import WSGIHandler
from django.core.servers.basehttp import WSGIRequestHandler
from wordnote.db.db import Create_cursor
from pathlib import Path

import toga


class ThreadedWSGIServer(socketserver.ThreadingMixIn, WSGIServer):
    pass


class wordnote(toga.App):
    def web_server(self):
        print("Starting server...")
        # Use port 0 to let the server select an available port.
        self._httpd = ThreadedWSGIServer(("127.0.0.1", 0), WSGIRequestHandler)
        self._httpd.daemon_threads = True

        os.environ["DJANGO_SETTINGS_MODULE"] = 'webapp.mysite.settings'
        django.setup(set_prefix=False)
        wsgi_handler = WSGIHandler()
        self._httpd.set_app(wsgi_handler)
        # The server is now listening, but connections will block until
        # serve_forever is run.
        self.server_exists.set()
        self._httpd.serve_forever()

    def cleanup(self, app, **kwargs):
        print("Shutting down...")
        self._httpd.shutdown()
        return True

    def on_key_press(widget, key, modifier):
        if key == toga.Key.ESCAPE:
            # Customize the behavior of the back button
            # For example, you can navigate to a specific screen or perform a specific action
            print("Back button pressed")

    def startup(self):
        self._impl.create_menus = lambda *x, **y: None

        home_dir = Path.home()
        db_path = home_dir / 'my_database.db'
        print(home_dir)
        # Create and initialize the database helper
        self.db_helper = Create_cursor(db_path)
        self.db_helper.create_connection()
        self.db_helper.create_table()
        self.db_helper.close_database()


        self.server_exists = Event()

        self.web_view = toga.WebView()

        self.server_thread = Thread(target=self.web_server)
        self.server_thread.start()

        self.on_exit = self.cleanup

        self.server_exists.wait()
        host, port = self._httpd.socket.getsockname()
        self.web_view.url = f"http://{host}:{port}/main_app"

        self.main_window = toga.MainWindow(title='')
        self.main_window.on_key_press = self.on_key_press
        self.main_window._is_full_screen = True

        self.main_window.content = self.web_view
        # self.formal_name
        self.main_window.show()


def main():
    return wordnote()
