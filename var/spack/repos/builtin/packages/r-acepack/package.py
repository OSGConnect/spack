# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RAcepack(RPackage):
    """ACE and AVAS for Selecting Multiple Regression Transformations."""

    homepage = "https://CRAN.R-project.org/package=acepack"
    url      = "https://cran.rstudio.com/src/contrib/acepack_1.4.1.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/acepack"

    version('1.4.1', 'a35354655e5260afa0e1860fcc68d871')
