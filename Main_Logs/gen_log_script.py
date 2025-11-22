from __future__ import annotations

import argparse
import datetime
import os
import random
from pathlib import Path
from typing import Iterable, List, Set, Dict


# Configuration / defaults
NAMES: List[str] = ['James', 'Dean', 'Alice', 'Doe']
EVENTS: List[str] = ['LOGON', 'LOGON_FAILED', 'LOGOFF', 'FILE_ACCESS']
IP_BASE = '10.1.1.'
IP_RANGE = range(2, 15)  # generates .2 .. .14
DEFAULT_LOG_NAME = 'logs.txt'
DEFAULT_MAX_COUNT = 1_000_000


def ensure_console_clear() -> None:
    """Clear the console (best-effort)."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def generate_ips() -> Set[str]:
    """Return a set of available IP addresses."""
    return {f'{IP_BASE}{i}' for i in IP_RANGE}


def assign_ips(names: Iterable[str], ips: Set[str]) -> Dict[str, str]:
    """Assign IPs to names. Prefer unique assignment when possible.

    If there are at least as many IPs as names, assigns unique IPs without
    replacement. Otherwise assigns with replacement.
    """
    names_list = list(names)
    if len(ips) >= len(names_list):
        chosen = random.sample(list(ips), k=len(names_list))
    else:
        # allow duplicates if there aren't enough IPs
        chosen = [random.choice(list(ips)) for _ in names_list]
    return dict(zip(names_list, chosen))


def gen_datetime() -> datetime.datetime:
    """Generate a random datetime on 2025-12-01.

    Kept simple to match previous behavior.
    """
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return datetime.datetime(2025, 12, 1, hour, minute, second)


def generate_timestamps(count: int) -> List[datetime.datetime]:
    """Generate up to `count` timestamps.

    This returns a sorted list of timestamps. Because the day has only 86400
    distinct seconds, duplicates are possible if `count` > 86400; duplicates
    are removed to keep unique timestamps.
    """
    timestamps: Set[datetime.datetime] = set()
    # keep producing until we have either `count` attempts or saturate unique
    attempts = 0
    while attempts < count:
        timestamps.add(gen_datetime())
        attempts += 1
        # small short-circuit: if we've reached all possible second-resolution
        # timestamps for the day, break.
        if len(timestamps) >= 24 * 60 * 60:
            break
    result = sorted(timestamps)
    return result


def write_logs(path: Path, timestamps: Iterable[datetime.datetime],
               workstation: Dict[str, str], *, names: Iterable[str] = NAMES,
               events: Iterable[str] = EVENTS) -> None:
    """Write the log lines to `path`.

    Each line: timestamp,name,ip,event
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8') as f:
        names_list = list(names)
        events_list = list(events)
        for ts in timestamps:
            name = random.choice(names_list)
            ip = workstation.get(name, '0.0.0.0')
            event = random.choice(events_list)
            f.write(f'{ts},{name},{ip},{event}\n')


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description='Generate synthetic logs')
    p.add_argument('--out', '-o', default=DEFAULT_LOG_NAME,
                   help='output log filename (created next to this script)')
    p.add_argument('--count', '-c', type=int, default=DEFAULT_MAX_COUNT,
                   help='number of timestamps to attempt to generate')
    p.add_argument('--pause', action='store_true',
                   help='pause and clear console before running')
    return p.parse_args(list(argv) if argv else None)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)

    if args.pause:
        input('Press Enter to continue...')
        ensure_console_clear()

    # Ensure output path is next to this script
    script_dir = Path(__file__).resolve().parent
    out_path = (script_dir / args.out).resolve()

    ips = generate_ips()
    workstation = assign_ips(NAMES, ips)
    timestamps = generate_timestamps(args.count)

    write_logs(out_path, timestamps, workstation)
    print(f'Wrote {len(timestamps)} entries to {out_path}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())