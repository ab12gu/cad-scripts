# Paint Stand Model

A 3D model of a paint stand created using build123d. This model includes a base, vertical support, and a circular holder for paint cans.

## Features

- **Base**: Wide, stable base with mounting holes
- **Support**: Vertical support with reinforcement ribs
- **Holder**: Circular ring with grip notches for easy paint can handling
- **Reinforcement**: Multiple reinforcement ribs for structural integrity

## Dimensions

- Base: 250mm × 180mm × 15mm
- Support: 25mm × 25mm × 350mm
- Holder: 140mm diameter, 50mm height
- Overall height: ~365mm

## Installation

1. Install the required dependency:
```bash
pip install -r requirements.txt
```

/Users/abhaygupta/Documents/code/cad-scripts/build123d/paint-stand

## Usage

Run the model generation script:
```bash
python paint_stand.py
```

This will create:
- `paint_stand.stl` - STL file for 3D printing
- `paint_stand.step` - STEP file for CAD software

## Model Functions

- `create_paint_stand()`: Basic paint stand model
- `create_advanced_paint_stand()`: Advanced model with additional features

## Customization

You can modify the dimensions in the functions to create custom paint stands for different paint can sizes or specific requirements.

## 3D Printing

The model is designed for 3D printing with:
- Appropriate wall thicknesses
- Support-free design
- Mounting holes for securing to surfaces
- Reinforced structure for stability 