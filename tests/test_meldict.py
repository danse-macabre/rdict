import nose
import rdict


def test_items():

    class AttrMap(rdict.MeldDict):
        def _meld(self, old_val, new_val, **meld_opts):
            return dict(new_val, **{k: old_val[k] for k in old_val if k not in new_val})

    mdict = AttrMap()
    mdict.occupy(0, 0x100, {'a': 1})
    mdict.occupy(0x180, 0x200, {'b': 2})
    mdict.occupy(0, 0x200, {'c': 3})

    nose.tools.assert_equal(list(mdict.irange()), [
        rdict.RangeItem(0, 0x100, {'a': 1, 'c': 3}),
        rdict.RangeItem(0x100, 0x180, {'c': 3}),
        rdict.RangeItem(0x180, 0x200, {'b': 2, 'c': 3}),
    ])


if __name__ == "__main__":
    test_items()
