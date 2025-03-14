"""Hello world func."""

import logging

from src.hello_world import hello_world

logger = logging.getLogger(__name__)


def main() -> None:
    """Return none."""
    hello_world()
    logger.info(hello_world())


if __name__ == "__main__":
    main()
