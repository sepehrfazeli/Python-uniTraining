import pytest

from fibonacci import fibonacci


def test_zero_input():
    # Arrange

    user_input = 0

    expected_result = 0

    # Act

    actual_result = fibonacci(user_input)

    # Assert

    assert actual_result == expected_result


def test_one_input():
    # Arrange

    user_input = 1

    expected_result = 1

    # Act

    actual_result = fibonacci(user_input)

    # Assert

    assert actual_result == expected_result


def test_negative_input():
    # Arrange

    user_input = -1

    expected_error = ValueError

    # Act

    with pytest.raises(expected_error) as e:
        fibonacci(user_input)

        # Assert

        assert str(e) == "n cannot be negative"


def test_positive_input_small():
    # arrange
    user_input = 6
    expected_result = 8

    # act
    actual_result = fibonacci(user_input)

    # assert
    assert expected_result == actual_result


def test_positive_input_medium():
    # arrange
    user_input = 10
    expected_result = 55

    # act
    actual_result = fibonacci(user_input)

    # assert
    assert expected_result == actual_result


def test_positive_input_big():
    # arrange
    user_input = 40
    expected_result = 102334155

    # act
    actual_result = fibonacci(user_input)

    # assert
    assert expected_result == actual_result
