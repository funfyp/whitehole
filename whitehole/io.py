"""Data I/O utilities"""

import numpy as np

import json

class PrimeDatabase:

@staticmethod

def load_from_file(filename):

with open(filename) as f:

return json.load(f)

class CMBDataLoader:

@staticmethod

def generate_mock_cmb(ell_max=2000):

ell = np.arange(2, ell_max + 1)

power = 5000 * np.exp(-(ell - 220)**2 / 10000) + 1000 * np.exp(-(ell - 550)**2 / 22500)

return ell, power