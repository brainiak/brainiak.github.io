# https://stackoverflow.com/questions/41520034/embed-jupyter-html-output-in-a-web-page
# Requires
# pip install nbconvert jupyter jupyter_client
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors.execute import CellExecutionError
import os

directory = "notebooks/tutorials"
for filename in os.listdir(directory):
    if filename.find("ipynb") > -1:
        src_notebook = nbformat.reads(open(os.path.join(directory, filename)).read(), as_version=4)

        # Uncomment to execute the notebook
        # ep = ExecutePreprocessor(timeout=50, kernel_name='python3')
        # ep.preprocess(src_notebook, {})
        html_exporter = HTMLExporter()
        html_exporter.template_file = 'full'
        (body, resources) = html_exporter.from_notebook_node(src_notebook)
        f = open(os.path.join(directory, filename.replace("ipynb", "html")), "w")
        f.write(body)
        f.close()
