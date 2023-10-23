import pytest


def test_main2():
    with pytest.raises(RuntimeError):
        raise RuntimeError
    assert True  # nosec B101
