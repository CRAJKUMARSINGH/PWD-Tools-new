# CustomTkinter Features

This project includes CustomTkinter-based desktop applications with magenta-themed styling.

## Files Created

1. `pwd_tools_ctk.py` - Full PWD Tools Hub desktop application using CustomTkinter
2. `demo_ctk_buttons.py` - Demonstration of CTkButton styling with magenta colors
3. `run_ctk_app.bat` - Batch file to run the main CTk application
4. `run_ctk_demo.bat` - Batch file to run the button styling demo

## Features

### Magenta Color Scheme
- Primary color: `#FF00FF` (Magenta)
- Hover color: `#CC00CC` (Darker magenta)
- Border color: `#FF66FF` (Lighter magenta)
- Various shades for different button styles

### Grid Layout
- 3-column grid layout for tool buttons
- Responsive design that adapts to window size
- Consistent spacing and padding

### CTkButton Styling
- Custom foreground colors
- Hover effects with color transitions
- Border styling options
- Rounded corners with configurable radius
- Consistent height and width for uniform appearance

## Installation

The CustomTkinter library will be automatically installed when running the batch files.
Alternatively, you can manually install it:

```bash
pip install customtkinter
```

## Running the Applications

### Main PWD Tools Application
```bash
# Direct Python execution
python pwd_tools_ctk.py

# Using batch file (Windows)
run_ctk_app.bat
```

### Button Styling Demo
```bash
# Direct Python execution
python demo_ctk_buttons.py

# Using batch file (Windows)
run_ctk_demo.bat
```

## Customization

You can customize the magenta color scheme by modifying the color values in the Python files:

- `fg_color` - Main button color
- `hover_color` - Color when hovering over the button
- `border_color` - Border color around the button

### Example Button with Magenta Styling
```python
button = ctk.CTkButton(
    master,
    text="Magenta Button",
    fg_color="#FF00FF",      # Magenta
    hover_color="#CC00CC",   # Darker magenta on hover
    border_width=2,
    border_color="#FF66FF"   # Lighter magenta border
)
```