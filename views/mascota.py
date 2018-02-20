#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request
from config.models import mascotas
from tinydb import Query

mascota_view = Bottle()