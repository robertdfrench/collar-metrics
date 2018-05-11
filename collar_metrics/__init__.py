import flask

def bootstrap(app):

    barks = []

    @app.route("/collar/1/barks", methods=['GET'])
    def list_barks():
        return flask.jsonify(data=barks)


    @app.route("/collar/1/barks/new", methods=['POST'])
    def add_bark():
        barks.append("crap")
        return flask.jsonify(data=barks)
