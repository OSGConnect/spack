# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
import sys


class Root(CMakePackage):
    """ROOT is a data analysis framework."""

    homepage = "https://root.cern.ch"
    url      = "https://root.cern.ch/download/root_v6.09.02.source.tar.gz"

    # Development versions
    version('6.09.02', '4188dfeafb72df339a3d688fe92f57ec')

    # Production versions
    version('6.08.06', 'bcf0be2df31a317d25694ad2736df268', preferred=True)

    # Old versions
    version('6.06.08', '6ef0fe9bd9f88f3ce8890e3651142ee4')
    version('6.06.06', '4308449892210c8d36e36924261fea26')
    version('6.06.04', '55a2f98dd4cea79c9c4e32407c2d6d17')
    version('6.06.02', 'e9b8b86838f65b0a78d8d02c66c2ec55')
    version('5.34.36', '6a1ad549b3b79b10bbb1f116b49067ee')

    if sys.platform == 'darwin':
        patch('math_uint.patch', when='@6.06.02')
        patch('root6-60606-mathmore.patch', when='@6.06.06')

    variant('graphviz', default=False, description='Enable graphviz support')

    depends_on('cmake@3.4.3:', type='build')
    depends_on('pkgconfig',   type='build')

    depends_on('binutils')
    depends_on('zlib')
    # depends_on('unuran')
    depends_on('freetype')
    depends_on('pcre')
    depends_on('xz')
    depends_on('libsm')
    depends_on('libice')
    depends_on('libx11')
    depends_on('libxext')
    depends_on('libxpm')
    depends_on('libxft')
    # depends_on('gif')
    depends_on('libpng')
    depends_on('jpeg')
    depends_on('gsl')
    depends_on('python@2.7:')
    # depends_on('opengl')
    depends_on('graphviz', when='+graphviz')
    # depends_on('kerberos')
    depends_on('libxml2+python')
    depends_on('openssl')
    # depends_on('castor')
    # depends_on('rfio')
    # depends_on('mysql')
    # depends_on('oracle')
    # depends_on('odbc')
    # depends_on('postgresql')
    depends_on('sqlite')
    # depends_on('pythia')
    depends_on('fftw')
    depends_on('cfitsio')
    # depends_on('monalisa')
    # depends_on('xrootd')
    # depends_on('gfal')
    # depends_on('dcap')
    # depends_on('ldap')
    # depends_on('chirp')
    # depends_on('hdfs')
    # depends_on('davix')

    # I was unable to build root with any Intel compiler
    # See https://sft.its.cern.ch/jira/browse/ROOT-7517
    conflicts('%intel')

    def cmake_args(self):
        args = [
            '-DCMAKE_CXX_FLAGS=-I/cvmfs/connect.opensciencegrid.org/modules/packages/linux-rhel7-x86_64/gcc-4.8.5spack/gcc-6.4.0-k5eggrz3xdhuomx6vhowwfis4spkuhfy/include/c++/6.4.0'
            '-Dcocoa=OFF',
            '-Dbonjour=OFF',
            '-Dx11=ON',
        ]

        if sys.platform == 'darwin':
            args.extend([
                '-Dcastor=OFF',
                '-Drfio=OFF',
                '-Ddcache=OFF',
            ])

        return args

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        spack_env.set('ROOTSYS', self.prefix)
        spack_env.set('ROOT_VERSION', 'v{0}'.format(self.version.up_to(1)))
        spack_env.prepend_path('PYTHONPATH', self.prefix.lib)
