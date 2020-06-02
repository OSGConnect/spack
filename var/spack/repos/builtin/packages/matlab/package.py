# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os
import subprocess


class Matlab(Package):
    """MATLAB (MATrix LABoratory) is a multi-paradigm numerical computing
    environment and fourth-generation programming language. A proprietary
    programming language developed by MathWorks, MATLAB allows matrix
    manipulations, plotting of functions and data, implementation of
    algorithms, creation of user interfaces, and interfacing with programs
    written in other languages, including C, C++, C#, Java, Fortran and Python.

    Note: MATLAB is licensed software. You will need to create an account on
    the MathWorks homepage and download MATLAB yourself. Spack will search your
    current directory for the download file. Alternatively, add this file to a
    mirror so that Spack can find it. For instructions on how to set up a
    mirror, see http://spack.readthedocs.io/en/latest/mirrors.html"""

    homepage = "https://www.mathworks.com/products/matlab.html" 
    version('R2018b', sha256='cc7f6e042c1b2edd5ae384c77d0b2c860e8dcfd7c5e23dbe07bf04d3a921e459')
    version('R2016b', 'b0e0b688894282139fa787b5a86a5cf7')

    variant(
        'mode',
        default='interactive',
        values=('interactive', 'silent', 'automated'),
        description='Installation mode (interactive, silent, or automated)'
    )

    variant(
        'key',
        default='',
        values=lambda x: True,  # Anything goes as a key
        description='The file installation key to use'
    )

    # Licensing
    license_required = False
    license_comment  = '#'
    license_files    = ['licenses/license.dat']
    license_vars     = ['LM_LICENSE_FILE']
    license_url      = 'https://www.mathworks.com/help/install/index.html'

    extendable = True

    def url_for_version(self, version):
        return "file://{0}/MCR_{1}_glnxa64_installer.zip".format(os.getcwd(), version)

    def configure(self, spec, prefix):
        config = {
            'destinationFolder':   prefix,
            'mode': 'silent',
            'agreeToLicense': 'yes'
        }

        # Store values requested by the installer in a file
        with open('spack_installer_input.txt', 'w') as input_file:
            for key in config:
                input_file.write('{0}={1}\n'.format(key, config[key]))

    def install(self, spec, prefix):
        self.configure(spec, prefix)

        # Run silent installation script
        # Full path required
        input_file = join_path(
            self.stage.source_path, 'spack_installer_input.txt')
        print(subprocess.call(['./install', '-inputFile', input_file]))
        subprocess.call(['./install', '-inputFile', input_file])

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('LD_LIBRARY_PATH', self.prefix + '/runtime/glnxa64')
        run_env.prepend_path('LD_LIBRARY_PATH', self.prefix + '/bin/glnxa64')
        run_env.prepend_path('LD_LIBRARY_PATH', self.prefix + '/sys/os/glnxa64')
        run_env.prepend_path('LD_LIBRARY_PATH', self.prefix + '/sys/opengl/lib/glnxa64')

