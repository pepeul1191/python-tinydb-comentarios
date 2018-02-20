#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request
from config.models import criadores
from config.middleware import response_headers, enable_cors
import time
from tinydb import Query

criador_view = Bottle()

@criador_view.route('/crear', method=['POST'])
@response_headers
@enable_cors
def crear():
	rpta = None
	try:
		criador = json.loads(request.query.criador)
		criador['comentarios'] = []
		comentario_id = criadores.insert(criador)
		rpta = {'tipo_mensaje' : 'success', 'mensaje' : ['Se ha aperturado los comentarios al criador', comentario_id]}
	except TypeError:
		rpta = {'tipo_mensaje' : 'error', 'mensaje' : ['Se ha producido un error en crear los comentarios del criador', str(e)]}	
	return json.dumps(rpta)

@criador_view.route('/comentar', method=['POST'])
@response_headers
@enable_cors
def comentar():
	rpta = None
	try:
		data = json.loads(request.query.data)
		Criador = Query()
		tmp = criadores.search(Criador.criador_id == data['comentario_criador_id'])
		comentario_nuevo = {'criador_id': data['criador_id'], 'comentario': data['comentario'], 'momento': time.time()}
		tmp = tmp[0]
		tmp['comentarios'].append(comentario_nuevo)
		criadores.upsert(tmp, Criador.criador_id == data['comentario_criador_id'])
		rpta = {'tipo_mensaje' : 'success', 'mensaje' : ['Ha comentado el perfil del criador']}
	except TypeError:
		rpta = {'tipo_mensaje' : 'error', 'mensaje' : ['Se ha producido un error en crear los comentarios del criador', str(e)]}	
	return json.dumps(rpta)