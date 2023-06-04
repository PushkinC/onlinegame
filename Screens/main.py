from App import App

if __name__ == '__main__':
    import Screens.InputScreen
    app = App('main')

    while app.running:
        app.tick()
