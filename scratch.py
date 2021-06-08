try:
    assert 'foo' < 'foo', 'on no'
    print('phew')
except Exception as e:
    print(e)