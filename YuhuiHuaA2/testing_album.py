"""Incomplete tests for Album class."""

from album import Album


def run_tests():
    """Test Album class."""

    # Test empty album (defaults)
    print("Test empty album:")
    empty_album = Album()
    print(empty_album)
    assert empty_album.title == ""
    assert empty_album.artist == ""
    assert empty_album.year == 0
    assert not empty_album.is_completed

    # Test initial-value album
    print("Test initial value album:")
    new_album = Album("Unleashed", "Skillet", 2016, False)
    # TODO: Write tests to show this initialisation works
    print(new_album)
    # Test mark_completed()
    # TODO: Write tests to show the mark_completed() method works
    print(new_album.mark_required())
    # TODO: Add tests for any untested methods (and more tests as needed)
    print(new_album.mark_completed())


run_tests()
