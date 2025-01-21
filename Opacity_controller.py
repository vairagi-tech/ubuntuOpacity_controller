import gi
gi.require_version("Gtk", "3.0")
gi.require_version("AppIndicator3", "0.1")
from gi.repository import Gtk, AppIndicator3
import subprocess

selected_window = None

def select_window():
    """Prompt user to click on a window and get its ID."""
    global selected_window
    try:
        print("Please select a window...")
        output = subprocess.check_output(["xprop", "-root", "_NET_ACTIVE_WINDOW"])
        window_id = output.decode().strip().split()[-1]
        selected_window = window_id
        print(f"Selected window: {window_id}")
        create_slider()
    except Exception as e:
        print(f"Error selecting window: {e}")

def set_window_opacity(opacity):
    """Set the opacity for the selected window."""
    if selected_window:
        hex_opacity = hex(int(opacity * 0xffffffff))[2:]  # Convert to hex
        subprocess.run(["xprop", "-id", selected_window, "-f", "_NET_WM_WINDOW_OPACITY", "32c", "-set", "_NET_WM_WINDOW_OPACITY", hex_opacity])

def create_slider():
    """Create a GTK slider for opacity control."""
    def on_opacity_changed(scale):
        value = scale.get_value()
        set_window_opacity(value / 100)  # Scale to [0, 1]

    window = Gtk.Window()
    window.set_title("Opacity Control")
    window.set_default_size(300, 50)
    window.set_position(Gtk.WindowPosition.CENTER)

    slider = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 100, 1)
    slider.set_value(100)  # Default to full opacity
    slider.connect("value-changed", on_opacity_changed)

    window.add(slider)
    window.show_all()
    Gtk.main()

def quit_app(widget, event):
    Gtk.main_quit()

def on_menu_item_selected(_):
    select_window()

def create_indicator():
    """Create a top-bar indicator with options."""
    indicator = AppIndicator3.Indicator.new(
        "OpacityController", "dialog-information", AppIndicator3.IndicatorCategory.APPLICATION_STATUS
    )
    indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)

    menu = Gtk.Menu()

    select_window_item = Gtk.MenuItem(label="Select Window")
    select_window_item.connect("activate", on_menu_item_selected)
    menu.append(select_window_item)

    quit_item = Gtk.MenuItem(label="Quit")
    quit_item.connect("activate", quit_app)
    menu.append(quit_item)

    menu.show_all()
    indicator.set_menu(menu)

if __name__ == "__main__":
    create_indicator()
    Gtk.main()