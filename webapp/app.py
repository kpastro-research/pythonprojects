from flask import Flask, render_template, request
import  whoami
import swimclub_dict
app = Flask(__name__)

SWIM_DATA_FOLDER="../swimdata"
log=False
all_swimclub_data=swimclub_dict.get_swim_data_dict(SWIM_DATA_FOLDER, 0,400,log)
all_swimclub_data_map=swimclub_dict.get_swimmer_data_map(all_swimclub_data,log)
@app.get('/')
def index():
    return render_template(
        "index.html",
        title="Welcome to the Swimclub system",
    )
    # return render_template('index.html')
@app.get('/allswimmers')
def all_swimmer():
    return all_swimclub_data_map
@app.get('/swimmers')
def swimmer_names():
    return render_template(
        "select.html",
        title="Select a swimmer",
        select_id="swimmer",
        url="/swimmer",
        data=sorted(all_swimclub_data_map),
    )
    # return sorted(all_swimclub_data_map)
    # return render_template('index.html')
@app.post('/swimmer')
def get_swimmer_by_name():
    swimmer = request.form["swimmer"]
    return render_template(
        "chart.html",
        title="Swim report for " + swimmer,
        swimmer_data=all_swimclub_data_map[swimmer],
    )

#
if __name__ == '__main__':
    app.run(debug=True)