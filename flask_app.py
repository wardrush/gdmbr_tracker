import flask
from flask import request, url_for, render_template, redirect
import utils

# Package needed data into dict for Jinja2 parsing
data = {
        "mapbox_access_token":utils.get_mapbox_accesskey(),
        "gdmbr_route_data":utils.get_route_data(),
        "current_long":-116,
        "current_lat":49
        }


app = flask.Flask(__name__)

@app.route('/',methods=['GET','POST'])
def my_maps():


  return render_template('index2.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)