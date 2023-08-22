from main import generate_filename


def test_generate_filename():
    assert (
        generate_filename(r' \ / : * ? " < > | \ ') == "           .mp4"
    ), "test 1 - special characters"
    assert (
        generate_filename(r"FIFTY FIFTY (피프티피프티) - 'Cupid' Official MV - YouTube")
        == "FIFTY FIFTY () - Cupid Official MV - YouTube.mp4"
    ), "test 2 - local characters (Korean)"
    assert (
        generate_filename(r"Из лета в осень, акварельные метаморфозы")
        == "Из лета в осень, акварельные метаморфозы.mp4"
    ), "test 3 - cyrillic"
    return True


if __name__ == "__main__":
    print(test_generate_filename())
