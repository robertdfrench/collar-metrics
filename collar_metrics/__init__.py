import flask


def bootstrap(app, barks):

    @app.route("/collar/<collar_id>/barks", methods=['GET'])
    def list_barks(collar_id):
        return flask.jsonify(data=barks.by_collar(collar_id))


    @app.route("/collar/<collar_id>/barks/new", methods=['POST'])
    def add_barks(collar_id):
        for bark in flask.request.json['data']:
            bark['attributes'].update(collar=collar_id)
            barks.add(**(bark['attributes']))
        return flask.jsonify(meta={'accepted': True})
