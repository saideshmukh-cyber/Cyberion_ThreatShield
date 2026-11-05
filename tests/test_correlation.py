
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

from scripts.correlation_engine import (
    evaluate_correlation,
    load_rules,
)


ROOT = Path(__file__).resolve().parents[1]
ALL_RULES = load_rules()


def load_correlation(filename):
    path = ROOT / "rules/correlation" / filename
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def make_event(timestamp, **fields):
    event = {
        "timestamp": timestamp.isoformat(),
    }
    event.update(fields)
    return event


def base_time():
    return datetime(2026, 11, 5, 12, 0, tzinfo=timezone.utc)


def test_failed_logon_burst_triggers_at_ten_events():
    rule = load_correlation("correlation_failed_logon_burst.yml")
    start = base_time()

    events = [
        make_event(
            start + timedelta(seconds=i * 20),
            EventID=4625,
            SourceIp="192.0.2.10",
            LogonType=3,
            host="WS-01",
        )
        for i in range(10)
    ]

    alerts = evaluate_correlation(rule, events, ALL_RULES)

    assert alerts
    assert alerts[-1]["count"] >= 10


def test_failed_logon_burst_does_not_trigger_at_nine():
    rule = load_correlation("correlation_failed_logon_burst.yml")
    start = base_time()

    events = [
        make_event(
            start + timedelta(seconds=i * 20),
            EventID=4625,
            SourceIp="192.0.2.10",
            LogonType=3,
            host="WS-01",
        )
        for i in range(9)
    ]

    alerts = evaluate_correlation(rule, events, ALL_RULES)

    assert not alerts


def test_failed_logons_from_different_ips_are_separate_groups():
    rule = load_correlation("correlation_failed_logon_burst.yml")
    start = base_time()

    events = []

    for i in range(10):
        events.append(
            make_event(
                start + timedelta(seconds=i * 10),
                EventID=4625,
                SourceIp=f"192.0.2.{i + 1}",
                LogonType=3,
                host="WS-01",
            )
        )

    alerts = evaluate_correlation(rule, events, ALL_RULES)

    assert not alerts


def test_dns_frequency_triggers_at_thirty_matching_queries():
    rule = load_correlation("correlation_dns_beaconing.yml")
    start = base_time()

    events = [
        make_event(
            start + timedelta(seconds=i * 10),
            query="suspicious-example.top",
            host="WS-DNS-01",
        )
        for i in range(30)
    ]

    alerts = evaluate_correlation(rule, events, ALL_RULES)

    assert alerts
    assert alerts[-1]["count"] >= 30


def test_dns_frequency_does_not_trigger_at_twenty_nine():
    rule = load_correlation("correlation_dns_beaconing.yml")
    start = base_time()

    events = [
        make_event(
            start + timedelta(seconds=i * 10),
            query="suspicious-example.top",
            host="WS-DNS-01",
        )
        for i in range(29)
    ]

    alerts = evaluate_correlation(rule, events, ALL_RULES)

    assert not alerts


def test_dns_queries_to_different_domains_are_separate_groups():
    rule = load_correlation("correlation_dns_beaconing.yml")
    start = base_time()

    events = [
        make_event(
            start + timedelta(seconds=i * 5),
            query=f"domain-{i}.top",
            host="WS-DNS-01",
        )
        for i in range(30)
    ]

    alerts = evaluate_correlation(rule, events, ALL_RULES)

    assert not alerts


def test_rdp_correlation_counts_distinct_hosts():
    rule = load_correlation("correlation_multi_host_rdp.yml")
    start = base_time()

    events = [
        make_event(
            start + timedelta(seconds=i * 20),
            EventID=4624,
            LogonType=10,
            SourceIp="198.51.100.50",
            host=f"SERVER-{i + 1}",
        )
        for i in range(5)
    ]

    alerts = evaluate_correlation(rule, events, ALL_RULES)

    assert alerts
    assert alerts[-1]["count"] >= 5


def test_rdp_correlation_does_not_trigger_at_four_hosts():
    rule = load_correlation("correlation_multi_host_rdp.yml")
    start = base_time()

    events = [
        make_event(
            start + timedelta(seconds=i * 20),
            EventID=4624,
            LogonType=10,
            SourceIp="198.51.100.50",
            host=f"SERVER-{i + 1}",
        )
        for i in range(4)
    ]

    alerts = evaluate_correlation(rule, events, ALL_RULES)

    assert not alerts


def test_rdp_repeated_logons_to_same_host_count_once():
    rule = load_correlation("correlation_multi_host_rdp.yml")
    start = base_time()

    events = [
        make_event(
            start + timedelta(seconds=i * 20),
            EventID=4624,
            LogonType=10,
            SourceIp="198.51.100.50",
            host="SERVER-01",
        )
        for i in range(10)
    ]

    alerts = evaluate_correlation(rule, events, ALL_RULES)

    assert not alerts


def test_failed_logons_outside_time_window_do_not_combine():
    rule = load_correlation("correlation_failed_logon_burst.yml")
    start = base_time()

    events = [
        make_event(
            start + timedelta(minutes=i * 6),
            EventID=4625,
            SourceIp="192.0.2.10",
            LogonType=3,
            host="WS-01",
        )
        for i in range(10)
    ]

    alerts = evaluate_correlation(rule, events, ALL_RULES)

    assert not alerts


def test_missing_timestamp_is_skipped():
    rule = load_correlation("correlation_failed_logon_burst.yml")

    events = [
        {
            "EventID": 4625,
            "SourceIp": "192.0.2.10",
            "LogonType": 3,
        }
        for _ in range(12)
    ]

    alerts = evaluate_correlation(rule, events, ALL_RULES)

    assert not alerts


def test_rdp_events_from_different_sources_do_not_combine():
    rule = load_correlation("correlation_multi_host_rdp.yml")
    start = base_time()

    events = [
        make_event(
            start + timedelta(seconds=i * 20),
            EventID=4624,
            LogonType=10,
            SourceIp=f"198.51.100.{i + 1}",
            host=f"SERVER-{i + 1}",
        )
        for i in range(5)
    ]

    alerts = evaluate_correlation(rule, events, ALL_RULES)

    assert not alerts
