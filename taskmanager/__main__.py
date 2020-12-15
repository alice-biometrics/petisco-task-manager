from petisco import Petisco

from taskmanager import petisco_setup, persistence_setup


def main():
    petisco_setup()
    persistence_setup()
    Petisco.get_instance().get_app()
    Petisco.get_instance().start()


if __name__ == "__main__":
    main()
