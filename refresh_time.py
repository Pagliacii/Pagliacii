#!/usr/bin/env python3

import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

tzinfo = timezone(timedelta(hours=8))  # CST: UTC+08:00
now = datetime.now(tzinfo)
readme = Path.cwd() / "README.md"
text = readme.read_text()
updated_text = re.sub(
    ">Last refresh: (\w+, \d+ \w+, \d+:\d+) CST<",
    f">Last refresh: {now.strftime('%A, %d %B, %H:%M')} CST<",
    text
)
readme.write_text(updated_text)
