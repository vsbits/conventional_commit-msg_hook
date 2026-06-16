import pytest

from commit_msg import abort
from commit_msg import extract_subject
from commit_msg import validate_subject


class TestValidateSubject:
    @pytest.mark.parametrize(
        "subject",
        [
            "feat: add new feature",
            "fix: resolve bug",
            "docs: update README",
            "feat(api): add endpoint",
            "fix(parser)!: change parsing behavior",
            "refactor(core): simplify logic",
            "chore!: breaking maintenance change",
        ],
    )
    def test_valid_subjects(self, subject):
        assert validate_subject(subject) is True

    @pytest.mark.parametrize(
        "subject",
        [
            "",
            "invalid commit",
            "feature: add new feature",  # invalid type
            "feat add feature",  # missing colon
            "feat:",  # missing description
            "feat(scope):",  # missing description
            ": description",  # missing type
        ],
    )
    def test_invalid_subjects(self, subject):
        assert validate_subject(subject) is False


class TestExtractSubject:
    def test_extracts_first_line(self):
        msg = """feat: add feature

More details here.
"""
        assert extract_subject(msg) == "feat: add feature"

    def test_ignores_blank_lines(self):
        msg = """



feat: add feature

body
"""
        assert extract_subject(msg) == "feat: add feature"

    def test_ignores_comment_lines(self):
        msg = """# Please enter the commit message
# On branch main

feat: add feature

body
"""
        assert extract_subject(msg) == "feat: add feature"

    def test_uses_first_non_comment_non_blank_line(self):
        msg = """

# comment

fix: bug fix
docs: another line
"""
        assert extract_subject(msg) == "fix: bug fix"

    def test_aborts_when_no_subject_exists(self):
        msg = """
# comment 1
# comment 2

"""
        with pytest.raises(SystemExit) as exc:
            extract_subject(msg)

        assert exc.value.code == 1


def test_abort_exits_with_code_1(capsys):
    with pytest.raises(SystemExit) as exc:
        abort("bad commit")

    assert exc.value.code == 1

    captured = capsys.readouterr()
    assert "" in captured.out
    assert "Invalid commit msg!" in captured.out
    assert "bad commit" in captured.out
    assert "Aborting..." in captured.out
