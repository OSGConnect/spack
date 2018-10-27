##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
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
#     spack install stashcache
#
# You can edit this file again by typing:
#
#     spack edit stashcache
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *

import os
import shutil

class Stashcache(Package):
    """
    Stashcp uses geo located nearby caches in order to copy from the OSG 
    Connect's stash storage service to a job's workspace on a cluster.
    """

    homepage = "https://github.com/opensciencegrid/StashCache"
    url      = "https://github.com/opensciencegrid/StashCache/archive/v5.0.0.tar.gz"

    version('5.1.2', '10af21499378eee03772bcc9436cb705')
    version('5.0.0', '89baccd756a4ec2f9c9eea64a97e26cf')

    depends_on('xrootd')

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        for f in os.listdir("bin"):
            src = join_path("bin", f)
            if os.path.isdir(src):
                dst = join_path(prefix.bin, f)
                shutil.copytree(src, dst)
            else:
                install(src, prefix.bin)
