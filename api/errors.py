from flask import Flask, render_template

def configure(app: Flask):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('not_found.html'), 404