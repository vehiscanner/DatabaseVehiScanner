from flask import Flask

app = Flask(__name__)

# Periksa direktori templates yang dikonfigurasikan
template_folder = app.template_folder

print("Direktori templates yang dikonfigurasikan:", template_folder)