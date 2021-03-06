#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import Bottle, run, HTTPResponse, static_file
from config.middleware import response_headers
from views.criador import criador_view
from views.mascota import mascota_view

app = Bottle()

@app.route('/')
@response_headers
def index():
	the_body = 'Error : URI vacía'
	return HTTPResponse(status=404, body=the_body)

@app.route('/test/conexion')
@response_headers
def test_conexion():
	return 'Ok'

@app.route('/:filename#.*#')
def send_static(filename):
  return static_file(filename, root='./static/')

if __name__ == '__main__':
	app.mount('/criador', criador_view)
	app.mount('/mascota', mascota_view)
	app.run(host='localhost', port=3031, debug=True, reloader=True)