import flask


def bootstrap(app, barks):

    @app.route("/collar/1/barks", methods=['GET'])
    def list_barks():
        return flask.jsonify(data=barks.by_collar('1'))


    @app.route("/collar/1/barks/new", methods=['POST'])
    def add_barks():
        for bark in flask.request.json['data']:
            bark['attributes'].update(collar='1')
            barks.add(**(bark['attributes']))
        return flask.jsonify(meta={'accepted': True})
