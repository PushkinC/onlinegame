from App import App

if __name__ == '__main__':
    app = App('main2')

    while app.running:
        app.tick()
