# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ants(CMakePackage):
    """ANTs extracts information from complex datasets that include imaging.
       Paired with ANTsR (answer), ANTs is useful for managing, interpreting
       and visualizing multidimensional data. ANTs is popularly considered a
       state-of-the-art medical image registration and segmentation toolkit.
       ANTs depends on the Insight ToolKit (ITK), a widely used medical image
       processing library to which ANTs developers contribute.
    """

    homepage = "http://stnava.github.io/ANTs/"
    url      = "https://github.com/ANTsX/ANTs/archive/v2.2.0.tar.gz"

    version('2.3.1', '75922052ef1cba832d7eb9e90a76688a')
    version('2.2.0', '5661b949268100ac0f7baf6d2702b4dd')

    depends_on('itk')
    depends_on('cmake')

    def install(self, spec, prefix):
        with working_dir(join_path('spack-build', 'ANTS-build'), create=False):
            make("install")
        install_tree('Scripts', prefix.bin)

    def setup_environment(self, spack_env, run_env):
        run_env.set('ANTSPATH', self.prefix.bin)
