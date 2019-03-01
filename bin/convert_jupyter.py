# https://stackoverflow.com/questions/41520034/embed-jupyter-html-output-in-a-web-page
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors.execute import CellExecutionError
src_notebook = nbformat.reads(open("notebooks/Test.ipynb").read(), as_version=4)   #where ff is file opened with some open("path to notebook file")

ep = ExecutePreprocessor(timeout=50, kernel_name='python3')
ep.preprocess(src_notebook, {})
html_exporter = HTMLExporter()
html_exporter.template_file = 'basic'  #basic will skip generating body and html tags.... use "all" to gen all..
(body, resources) = html_exporter.from_notebook_node(src_notebook)
print(body)   #body have html output
