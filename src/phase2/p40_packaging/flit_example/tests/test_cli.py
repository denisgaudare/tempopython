from mypkg.cli import main

def test_main(capfd):
    main()
    out, _ = capfd.readouterr()
    assert "Hello from mypkg" in out
