''' NMR metabolite standards library processing '''

import os.path

import nmrglue as ng
#import numpy as np

def read_spectrum(path):
    '''
    Reads a processed Bruker NMR spectrum file
    '''
    if os.path.exists(path):
        dic, spec = ng.bruker.read(path)
    else:
        print('file %s not found..skipping' % path)

    return [os.path.basename(path), dic, spec]

def read_spectra(pathlist):
    '''
    Reads a library of Bruker NMR spectra of metabolite standards.
    '''
    spectra = [read_spectrum(path) for path in pathlist]
    return spectra

def process_spectra(specs):
    '''
    Preprocessing of NMR spectra prior to synthesis.
    '''
    pass

def write_spectra_file(specs, path, frmt='pickle'):
    '''
    Writes spectral library to file (.csv, pickle (recommended)).
    '''
    pass
