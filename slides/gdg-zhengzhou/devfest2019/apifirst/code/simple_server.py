def index():
    return {
        'data': 'Hello World'
    }

def test_should_return_hello_world_when_access_index():
    assert 'Hello World' == index().get('data')

if __name__ == "__main__":
    test_should_return_hello_world_when_access_index()