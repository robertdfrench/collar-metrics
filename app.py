import flask
from collar_metrics import barks_table
import collar_metrics


app = flask.Flask(__name__)
collar_metrics.bootstrap(app, barks_table.BarksTable())
