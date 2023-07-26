import sys


def test_main(capsys):
    sys.argv = ['h', 'H', 'help']
    main()
    out, err = capsys.readouterr()
    assert
