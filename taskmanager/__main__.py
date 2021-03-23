import os

from petisco import Petisco

from taskmanager.petisco_loader import load


def main():
    if not os.getenv("END2END_TEST"):
        load(testing=True)
    else:
        load()
    Petisco.get_instance().get_app()
    Petisco.get_instance().start()


if __name__ == "__main__":
    main()
