# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ape(Package):
    """A tool for generating atomic pseudopotentials within a Density-Functional
    Theory framework"""

    homepage = "http://www.tddft.org/programs/APE/"
    url      = "http://www.tddft.org/programs/APE/sites/default/files/ape-2.2.1.tar.gz"

    version('2.2.1', 'ab81da85bd749c0c136af088c7f9ad58')

    depends_on('gsl')
    depends_on('libxc@:2.2.2')

    def install(self, spec, prefix):
        args = []
        args.extend([
            '--prefix=%s' % prefix,
            '--with-gsl-prefix=%s'   % spec['gsl'].prefix,
            '--with-libxc-prefix=%s' % spec['libxc'].prefix
        ])

        # When preprocessor expands macros (i.e. CFLAGS) defined as quoted
        # strings the result may be > 132 chars and is terminated.
        # This will look to a compiler as an Unterminated character constant
        # and produce Line truncated errors. To vercome this, add flags to
        # let compiler know that the entire line is meaningful.
        # TODO: For the lack of better approach, assume that clang is mixed
        # with GNU fortran.
        if spec.satisfies('%clang') or spec.satisfies('%gcc'):
            args.extend([
                'FCFLAGS=-O2 -ffree-line-length-none'
            ])

        configure(*args)
        make()
        make('install')
