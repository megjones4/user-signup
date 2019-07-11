from flask import Flask, request, redirect, render_template
import jinja2
import os 

app = Flask(__name__)
app.config['DEBUG'] = True 

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))


@app.route("/")
def index():
  template = jinja_env.get_template("index.html")
  return template.render()

app.run()
