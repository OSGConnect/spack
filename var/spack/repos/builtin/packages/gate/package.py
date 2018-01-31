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
#     spack install gate
#
# You can edit this file again by typing:
#
#     spack edit gate
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *
import platform


class Gate(CMakePackage):
    """Numerical simulations package for use in medical imaging and radiotherapy."""

    homepage = "http://www.opengatecollaboration.org/"
    #url      = "http://www.opengatecollaboration.org/sites/default/files/gate_v7.2.tar.gz"
    url      = "https://github.com/OpenGATE/Gate/archive/v8.0.zip"

    #version('7.2', 'ae399c0af959846c018069d554fd05a9')
    #version('7.2', '02816b66f4fcf49200bfb6caae51ba66')
    version('8.0', '5914ac7a93ef02b10943f850c4473429')

    variant('cxx11', default=True, description="Compile using c++11 dialect.")

    depends_on('cmake@3.5:', type='build')

    depends_on('root')

    depends_on('geant4@10.03.p03+cxx11~cxx14~mt', when='@8.0+cxx11')
    depends_on('clhep@2.3.4.3+cxx11~cxx14', when='@8.0+cxx11')

    def cmake_args(self):
        spec = self.spec

        options = []

        if '+cxx11' in spec:
            options.append('-DGATE_USE_STDC11=ON')

        return options

