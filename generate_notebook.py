"""Generate Jupyter notebooks"""

import json

def create_quick_start():

cells = [

{"cell_type": "markdown", "metadata": {}, "source": ["# WhiteHole Quick Start"]},

{"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],

"source": ["from whitehole import *\\nimport numpy as np"]},



nb = {"cells": cells, "metadata": {}, "nbformat": 4, "nbformat_minor": 4}

return json.dumps(nb, indent=2)

if __name__ == "__main__":

print(create_quick_start())