import nose
import rdict


def test_items():
    rangedict = rdict.RangeDict()
    rangedict[0:10] = 'a'
    rangedict[5:15] = 'b'
    nose.tools.assert_equal(len(rangedict), 2)
    nose.tools.assert_equal(rangedict[0:5], ['a'])
    nose.tools.assert_equal(rangedict[5:15], ['b'])

    rangedict = rdict.RangeDict()
    rangedict[0:15] = 'a'
    rangedict[-5:10] = 'b'
    nose.tools.assert_equal(len(rangedict), 2)
    nose.tools.assert_equal(rangedict[-5:10], ['b'])
    nose.tools.assert_equal(rangedict[10:15], ['a'])

    rangedict = rdict.RangeDict()
    rangedict[0:10] = 'a'
    rangedict[-5:15] = 'b'
    nose.tools.assert_equal(len(rangedict), 1)
    nose.tools.assert_equal(rangedict[-5:15], ['b'])

    rangedict = rdict.RangeDict()
    rangedict[-5:15] = 'a'
    rangedict[0:10] = 'b'
    nose.tools.assert_equal(len(rangedict), 3)
    nose.tools.assert_equal(rangedict[-5:0], ['a'])
    nose.tools.assert_equal(rangedict[0:10], ['b'])
    nose.tools.assert_equal(rangedict[10:15], ['a'])

    rangedict = rdict.RangeDict()
    rangedict[0:5] = 'a'
    rangedict[10:15] = 'a'
    rangedict[5:10] = 'a'
    nose.tools.assert_equal(len(rangedict), 1)
    nose.tools.assert_equal(rangedict[0:15], ['a'])

    rangedict = rdict.RangeDict()
    rangedict[0:5] = 'b'
    rangedict[10:15] = 'a'
    rangedict[5:10] = 'a'
    nose.tools.assert_equal(len(rangedict), 2)
    nose.tools.assert_equal(rangedict[0:5], ['b'])
    nose.tools.assert_equal(rangedict[5:15], ['a'])

    rangedict = rdict.RangeDict()
    rangedict[0:5] = 'b'
    rangedict[5:10] = 'a'
    rangedict[3:8] = 'c'
    nose.tools.assert_equal(len(rangedict), 3)
    nose.tools.assert_equal(rangedict[0:3], ['b'])
    nose.tools.assert_equal(rangedict[3:8], ['c'])
    nose.tools.assert_equal(rangedict[8:10], ['a'])


if __name__ == "__main__":
    test_items()
