from App import App

if __name__ == '__main__':
    app = App('main3')

    while app.running:
        app.tick()
