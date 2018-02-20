#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request
from config.models import criadores
from tinydb import Query

criador_view = Bottle()