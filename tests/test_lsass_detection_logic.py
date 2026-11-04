def matches_lsass_rule(event):
    target = event.get("TargetImage", "").lower()
    access = event.get("GrantedAccess", "").lower()

    target_matches = target.endswith("\\lsass.exe")

    suspicious_access_masks = {
        "0x1010",
        "0x1410",
        "0x1438",
        "0x143a",
    }

    return target_matches and access in suspicious_access_masks


def test_detects_powershell_access_to_lsass():
    event = {
        "SourceImage": r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe",
        "TargetImage": r"C:\Windows\System32\lsass.exe",
        "GrantedAccess": "0x1010",
    }

    assert matches_lsass_rule(event)


def test_detects_case_insensitive_lsass_path():
    event = {
        "SourceImage": r"C:\Tools\unknown.exe",
        "TargetImage": r"C:\WINDOWS\SYSTEM32\LSASS.EXE",
        "GrantedAccess": "0x1410",
    }

    assert matches_lsass_rule(event)


def test_does_not_detect_access_to_other_process():
    event = {
        "SourceImage": r"C:\Tools\unknown.exe",
        "TargetImage": r"C:\Windows\System32\notepad.exe",
        "GrantedAccess": "0x1010",
    }

    assert not matches_lsass_rule(event)


def test_does_not_detect_unlisted_access_mask():
    event = {
        "SourceImage": r"C:\Tools\unknown.exe",
        "TargetImage": r"C:\Windows\System32\lsass.exe",
        "GrantedAccess": "0x1000",
    }

    assert not matches_lsass_rule(event)


def test_does_not_detect_missing_target():
    event = {
        "SourceImage": r"C:\Tools\unknown.exe",
        "GrantedAccess": "0x1010",
    }

    assert not matches_lsass_rule(event)
