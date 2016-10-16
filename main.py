from app import Factory


def main():
    app_manager = Factory.get_app_manager()
    app_manager.init_dirs()
    app_manager.create_app()


if __name__ == '__main__':
    main()
