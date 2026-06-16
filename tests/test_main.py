from unittest.mock import mock_open
from unittest.mock import patch

import pytest

from commit_msg import main


def test_main_valid_commit(monkeypatch):
    monkeypatch.setattr("sys.argv", ["script", "COMMIT_MSG"])

    m = mock_open(read_data="feat: add feature")
    with patch("builtins.open", m):
        main()


def test_main_invalid_commit(monkeypatch):
    monkeypatch.setattr("sys.argv", ["script", "COMMIT_MSG"])

    m = mock_open(read_data="not a conventional commit")
    with patch("builtins.open", m):
        with pytest.raises(SystemExit) as exc:
            main()

    assert exc.value.code == 1
