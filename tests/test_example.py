from pathlib import Path
import sys

# Add src/ directory to the module search path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from example import add


def test_add():
    assert add(2, 3) == 5
