''' Tests for ProcessNMRLibrary module'''

from nose.tools import *
import simNMR.ProcessNMRLibrary as pl

def test_read_nmr():
    '''tests for nmr reading function'''

    spec = pl.read_spectrum('tests/data/Glutamine')

    assert_equal(len(spec), 3)
    assert_equal(spec[0], 'Glutamine')


