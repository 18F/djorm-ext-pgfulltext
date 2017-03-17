import psycopg2

from django.db import connection
from django.utils.text import force_text


def adapt(text):
    connection.ensure_connection()
    a = psycopg2.extensions.adapt(force_text(text))
    c = connection.connection

    # This is a workaround for https://github.com/18F/calc/issues/1498.
    if hasattr(c, '__wrapped__'):
        c = getattr(c, '__wrapped__')

    a.prepare(c)
    return a
