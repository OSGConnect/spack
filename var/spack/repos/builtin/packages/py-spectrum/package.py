##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-spectrum
#
# You can edit this file again by typing:
#
#     spack edit py-spectrum
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PySpectrum(PythonPackage):
    """
    Spectrum contains tools to estimate Power Spectral Densities 
    using methods based on Fourier transform, Parametric methods,
    or eigenvalues analysis
    """

    homepage = "https://pyspectrum.readthedocs.io/en/latest/"
    url      = "https://files.pythonhosted.org/packages/source/s/spectrum/spectrum-0.7.3.tar.gz"

    version('0.7.3', '62f0441eae1c889cadd7caa21b1499b6')

    depends_on('py-setuptools', type='build')
    depends_on('py-numpy')
    depends_on('py-scipy')
    depends_on('py-matplotlib')
   

