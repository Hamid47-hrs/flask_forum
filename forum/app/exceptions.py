from flask import render_template


def forbidden_access(e):
    return render_template("exceptions/403.html"), 403


def page_not_found(e):
    return render_template("exceptions/404.html"), 404


def deleted_page(e):
    return render_template("exceptions/410.html"), 410


def server_error(e):
    return render_template("exceptions/500.html"), 500
