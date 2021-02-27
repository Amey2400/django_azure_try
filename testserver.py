from django.conf import settings
import deploytestserver.settings as app_settings

#settings.configure(INSTALLED_APPS=app_settings.INSTALLED_APPS,DATABASES=app_settings.DATABASES)

import django
django.setup()

import json
from api.models import outputplot
import sys

import numpy as np
import matplotlib.pyplot as plt
import math
import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()


from PySpice.Plot.BodeDiagram import bode_diagram
from PySpice.Probe.Plot import plot
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

####################################################################################################

from PySpice.Spice.Netlist import SubCircuitFactory
from PySpice.Unit import *
#to avoid warnings
import warnings
warnings.filterwarnings("ignore")
def sample():
  outputplot.objects.update_or_create(id=20, x="helloPython")


