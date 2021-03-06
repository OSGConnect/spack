# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RPsych(RPackage):
    """A general purpose toolbox for personality, psychometric theory and
       experimental psychology. Functions are primarily for multivariate
       analysis and scale construction using factor analysis, principal
       component analysis, cluster analysis and reliability analysis, although
       others provide basic descriptive statistics. Item Response Theory is
       done using factor analysis of tetrachoric and polychoric correlations.
       Functions for analyzing data at multiple levels include within and
       between group statistics, including correlations and factor analysis.
       Functions for simulating and testing particular item and test structures
       are included. Several functions serve as a useful front end for
       structural equation modeling. Graphical displays of path diagrams,
       factor analysis and structural equation models are created using basic
       graphics. Some of the functions are written to support a book on
       psychometric theory as well as publications in personality research.
       For more information, see the <http://personality-project.org/r> web
       page."""

    homepage = "http://personality-project.org/r/psych"
    url      = "https://cran.r-project.org/src/contrib/psych_1.7.8.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/psych"

    version('1.7.8', 'db37f2f85ff5470ee40bbc0a58ebe22b')

    depends_on('r-mnormt', type=('build', 'run'))
    depends_on('r-foreign', type=('build', 'run'))
    depends_on('r-lattice', type=('build', 'run'))
    depends_on('r-nlme', type=('build', 'run'))
