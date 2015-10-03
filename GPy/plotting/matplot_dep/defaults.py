#===============================================================================
# Copyright (c) 2015, Max Zwiessele
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# * Neither the name of GPy nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#===============================================================================
'''
This file is for defaults for the gpy plot, specific to the plotting library.

Create a kwargs dictionary with the right name for the plotting function 
you are implementing. If you do not provide defaults, the default behaviour of
the plotting library will be used. 

In the code, always ise plotting.gpy_plots.defaults to get the defaults, as 
it gives back an empty default, when defaults are not defined.
'''

from matplotlib import cm
from . import Tango

# Data:
data_1d = dict(lw=1.5, marker='x', edgecolor='k')
data_2d = dict(s=35, edgecolors='none', linewidth=0., cmap=cm.get_cmap('hot'))
xerrorbar = dict(ecolor='k', fmt='none', elinewidth=.5, alpha=.5)
yerrorbar = dict(ecolor=Tango.colorsHex['darkBlue'], fmt='none', elinewidth=.5, alpha=.5)

# GP plots
meanplot_1d = dict(color=Tango.colorsHex['mediumBlue'], linewidth=2)
meanplot_2d = dict(cmap='hot', linewidth=.5)
confidence_interval = dict(linecolor=Tango.colorsHex['darkBlue'],fillcolor=Tango.colorsHex['lightBlue'])