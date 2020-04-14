from petisco import Petisco

from taskmanager import petisco_setup


def main():
    petisco_setup()
    Petisco.get_instance().start()


if __name__ == "__main__":
    main()
