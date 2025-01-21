# Opacity Controller

Opacity Controller is a Python application that allows you to control the opacity of any window on your desktop using a GTK slider. It provides a system tray indicator for easy access to the opacity control functionality.

## Features

- Select any window to control its opacity.
- Adjust the opacity of the selected window using a GTK slider.
- System tray indicator for quick access.
- Quit option to exit the application.

## Requirements

- Python 3
- GTK 3
- AppIndicator3
- `xprop` (X11 utility)

## Installation

1. Install the required dependencies:
    ```sh
    sudo apt-get install python3-gi gir1.2-gtk-3.0 gir1.2-appindicator3-0.1 x11-utils
    ```

2. Clone the repository:
    ```sh
    git clone https://github.com/vairagi-tech/opacity-controller.git
    cd opacity-controller
    ```

## Usage

1. Run the application:
    ```sh
    python3 Opacity_controller.py
    ```

2. Click on the system tray indicator and select "Select Window".
3. Click on the window you want to control.
4. Adjust the opacity using the slider that appears.

## Code Overview

- [select_window()](http://_vscodecontentref_/0): Prompts the user to click on a window and retrieves its ID.
- [set_window_opacity(opacity)](http://_vscodecontentref_/1): Sets the opacity for the selected window.
- [create_slider()](http://_vscodecontentref_/2): Creates a GTK slider for opacity control.
- [quit_app(widget, event)](http://_vscodecontentref_/3): Quits the application.
- [on_menu_item_selected(_)](http://_vscodecontentref_/4): Callback for the "Select Window" menu item.
- [create_indicator()](http://_vscodecontentref_/5): Creates a system tray indicator with options.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Author

[Abhay kumar](https://github.com/vairagi-tech)