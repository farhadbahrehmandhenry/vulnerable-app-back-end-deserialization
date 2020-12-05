import pickle
import os
import time
import re

from flask import Blueprint, jsonify, request
from base64 import b64encode, b64decode

main = Blueprint('main', __name__)

@main.route('/api/vulnerable/bad/deserialization', methods=['POST'])
def addBad():
  user = request.get_json()
  serialized = b64encode(pickle.dumps(user))
  pickle.dump(user, open('track_file','wb'))
  deserialized = pickle.load(open('track_file','rb'))
  print(user, deserialized)

  return {'serialized': str(serialized), 'deserialized': deserialized}

@main.route('/api/vulnerable/good/deserialization', methods=['POST'])
def addGood():
  user = request.get_json()
  if not re.search('[#()=>^]', user['userName']) and not re.search('[#()=>^]', user['password']):
    serialized = b64encode(pickle.dumps(user))
    pickle.dump(user, open('track_file','wb'))
    deserialized = pickle.load(open('track_file','rb'))

    return {'serialized': str(serialized), 'deserialized': deserialized, 'type': 'success'}
  else :
    return {'serialized': '', 'deserialized': '', 'type': 'error'}
