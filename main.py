from evottt import Config, Manager

if __name__ == "__main__":
    config = Config()
    manager = Manager(config)
    manager.initialize()
    manager.run()
