#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request
from config.models import criadores
from config.middleware import response_headers, enable_cors
#from tinydb import Query

criador_view = Bottle()

@criador_view.route('/crear', method=['GET'])
@response_headers
def crear():
	rpta = None
	try:
		criador = json.loads(request.query.criador)
		comentario_id = criadores.insert(criador)
		rpta = {'tipo_mensaje' : 'success', 'mensaje' : ['Se ha aperturado los comentarios al criador', comentario_id]}
	except TypeError:
		rpta = {'tipo_mensaje' : 'error', 'mensaje' : ['Se ha producido un error en crear los comentarios del criador', str(e)]}	
	return json.dumps(rpta)