__all__ = ['get_version']


def get_version(version):
    _version = '%s.%s' % (version[0], version[1])
    if version[2]:
        _version = '%s.%s' % (_version, version[2])
    if version[3:] == ('alpha', 0):
        _version = '%s pre-alpha' % version
    else:
        if version[3] != 'final':
            _version = "%s %s" % (_version, version[3])
            if version[4] != 0:
                _version = '%s %s' % (_version, version[4])
    return _version
