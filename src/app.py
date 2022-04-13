from flask import Flask, request

from database import db_connection

app = Flask(__name__)


@app.get("/")
def overview():
    sql = request.args.get("sql", None)
    if sql is None or sql == "":
        return "No request given"

    db = db_connection()
    cur = db.cursor()
    return cur.execute(sql)
