#!/usr/bin/env python3.6

from realhome.app import App


def main():
    app = App(debug=True)
    with app as a:
        a.run()


if __name__ == "__main__":
    main()
