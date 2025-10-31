"""Tests for core module"""

import pytest

import numpy as np

from whitehole.core import BlackWhiteHoleSystem, SuperpositionState

def test_schwarzschild_outside_horizon():

"""Test metric outside event horizon"""

bh = BlackWhiteHoleSystem(mass=1.0)

metric = bh.schwarzschild_metric(r=10.0)

assert metric['g_rr'] > 0

assert metric['g_tt'] < 0

def test_superposition_normalization():

"""Test superposition state normalization"""

psi = SuperpositionState()

norm = np.linalg.norm(psi.state_vector())

assert np.isclose(norm, 1.0)

def test_density_matrix_hermitian():

"""Test density matrix is Hermitian"""

psi = SuperpositionState()

rho = psi.density_matrix()

assert np.allclose(rho, rho.conj().T)