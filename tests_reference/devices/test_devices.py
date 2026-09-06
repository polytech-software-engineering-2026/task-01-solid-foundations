from tests_reference.conftest import import_solution

SimplePrinter, AllInOnePrinter = import_solution(
    "katas.devices.solution", "SimplePrinter", "AllInOnePrinter"
)


def test_simple_printer_prints_without_raising() -> None:
    SimplePrinter().print_doc("hello")


def test_simple_printer_has_no_scan_method() -> None:
    assert not hasattr(SimplePrinter, "scan_doc"), (
        "SimplePrinter не должен иметь scan_doc — см. task.md про ISP"
    )


def test_simple_printer_has_no_fax_method() -> None:
    assert not hasattr(SimplePrinter, "send_fax"), (
        "SimplePrinter не должен иметь send_fax — см. task.md про ISP"
    )


def test_all_in_one_prints_without_raising() -> None:
    AllInOnePrinter().print_doc("hello")


def test_all_in_one_scans_returns_string() -> None:
    assert isinstance(AllInOnePrinter().scan_doc(), str)


def test_all_in_one_sends_fax_without_raising() -> None:
    AllInOnePrinter().send_fax("hello", "+70000000000")
