"""
© 2021 Preocts

This work ‘as-is’ I provide.
No warranty express or implied.
  For no purpose fit,
  not even a wee bit.
Liability for damages denied.

Permission is granted hereby,
to copy, share, and modify.
  Use it with glee,
  for profit or free.
On this notice, these rights rely.
"""
import logging


class CheckStringLength:
    log = logging.getLogger(__name__)

    @staticmethod
    def checkstringlength(string: str, length: int) -> bool:
        """Check if string is desired length, returns True or False"""

        string = str(string)
        length = int(length)

        if isinstance(string, str) and len(string):
            list_of_string = list(string)
            counter = 0
            idx = 0
            error = False

            while not bool(error):
                if idx >= len(list_of_string) or not (list_of_string[idx]):
                    error = True
                    continue
                counter += 1
                idx += 1

            CheckStringLength.log.debug("%s %s -- %s %s", string, length, counter, list_of_string)

            if counter == length:
                return True

            if counter != length:
                return False

        elif not isinstance(string, str) or not len(string):
            return False


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")

    print('"", 10 -- ' + str(CheckStringLength.checkstringlength("", 10)))
    print(
        "Hello World, 10 -- "
        + str(CheckStringLength.checkstringlength("Hello World", 10))
    )
    print(
        "Hello World, 11 -- "
        + str(CheckStringLength.checkstringlength("Hello World", 11))
    )
