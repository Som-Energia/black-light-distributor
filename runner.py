from server import build_app


# Manual runner for development
if __name__ == '__main__':
    app = build_app()
    app.run()
