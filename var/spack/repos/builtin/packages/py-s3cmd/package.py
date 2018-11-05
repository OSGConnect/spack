# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-s3cmd
#
# You can edit this file again by typing:
#
#     spack edit py-s3cmd
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyS3cmd(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/s3tools/s3cmd/archive/v2.0.2.tar.gz"

    version('2.0.2', sha256='50e11a040f97c08b5a80fe28a21ac337f5d62deeddfdf14bb6543e911b273347')
    version('2.0.1', sha256='92d2582a5a3771e9bb3a552b5bdc00b4a1cc6e8b735abac225f1c97a86f6d3b7')
    version('2.0.0', sha256='bf2a50802f1031cba83e99be488965803899d8ab0228c800c833b55c7269cd48')
    version('1.6.1', sha256='e3b962e94068230d4e3ec15b4e827e76cbe7e51dda0e80697ebffbe20b15098b')

    # FIXME: Add dependencies if required.
    depends_on('py-setuptools')

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
