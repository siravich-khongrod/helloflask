from flask import Flask, request, abort, render_template
import requests

app = Flask(__name__,template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def render_sr():
#	task = [task for task in tasks if task['id'] == task_id]
#    if len(task) == 0:
#        abort(404)
	url = 'https://secure-woodland-20008.herokuapp.com/search?q=i%20love%%20electrical%20engineering'
	r = requests.get(url)
	return render_template('search_results.html', results=r.json())
    #return jsonify({'sr': content})

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)