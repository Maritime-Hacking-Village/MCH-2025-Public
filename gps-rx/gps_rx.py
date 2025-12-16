from serial import Serial
from devtools import debug
import os
import time
import pynmea2
import sys

def main(av: list[str]) -> int:
  if len(av) != 2:
    print("Usage: gps_rx.py DEV", file=sys.stderr)
    return os.EX_USAGE
  
  with Serial(av[1], 9600, timeout=3) as stream:
    for line in stream:
      try:
        line_str = line.decode("utf8")
        msg = pynmea2.parse(line_str)
        # debug(time.time(), line_str, msg)
        print(line_str.strip())
      except pynmea2.ParseError as exc:
        debug(time.time(), exc)
        continue

  return os.EX_OK

if __name__ == "__main__":
  try:
    sys.exit(main(sys.argv))
  except KeyboardInterrupt:
    pass
