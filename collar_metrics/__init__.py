import flask


def bootstrap(app, barks):

    @app.route("/collar/1/barks", methods=['GET'])
    def list_barks():
        return flask.jsonify(data=barks)


    @app.route("/collar/1/barks/new", methods=['POST'])
    def add_barks():
        for bark in flask.request.json['data']:
            barks.append(bark)
        return flask.jsonify(data=barks)
