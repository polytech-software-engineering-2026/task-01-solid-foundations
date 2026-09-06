import pytest

from tests_reference.conftest import import_solution

EmailNotifier, SmsNotifier = import_solution(
    "katas.notifications.solution", "EmailNotifier", "SmsNotifier"
)

IMPLEMENTATIONS = [EmailNotifier, SmsNotifier]


@pytest.mark.parametrize("cls", IMPLEMENTATIONS)
def test_send_returns_true_on_valid_input(cls: type) -> None:
    assert cls().send("hello", "someone") is True


@pytest.mark.parametrize("cls", IMPLEMENTATIONS)
def test_send_raises_on_empty_message(cls: type) -> None:
    with pytest.raises(ValueError):
        cls().send("", "someone")


@pytest.mark.parametrize("cls", IMPLEMENTATIONS)
def test_send_raises_on_empty_recipient(cls: type) -> None:
    with pytest.raises(ValueError):
        cls().send("hello", "")


@pytest.mark.parametrize("cls", IMPLEMENTATIONS)
def test_send_returns_bool_not_truthy_object(cls: type) -> None:
    assert cls().send("hello", "someone") in (True, False)


def test_implementations_are_interchangeable_behind_the_same_call() -> None:
    def notify_all(notifiers: list, message: str, recipient: str) -> list[bool]:
        return [n.send(message, recipient) for n in notifiers]

    results = notify_all([EmailNotifier(), SmsNotifier()], "hi", "someone")
    assert results == [True, True]
