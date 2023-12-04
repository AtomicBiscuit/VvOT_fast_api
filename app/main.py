from fastapi_module import app
from uvicorn import run


def main():
    run(app, host='0.0.0.0', port=8050)


if __name__ == '__main__':
    main()
