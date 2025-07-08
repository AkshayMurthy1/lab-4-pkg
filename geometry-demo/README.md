# Geometry Demo

Geometry Demo serves as a practice project to better understand how to create reproducible packages that are user-friendly. It aids in solving high school level geometry problems, involving area and stats about various area shapes and tasks with an OOP structure.

## Installation

Follow the below steps to use the github to install this package.

1. Clone this git repo through `git clone <repo_name>`
2. Make sure you are in the geometry-demo folder. Install packages through `pip install -e .`
3. Import all wanted packages through `import geometry-demo`


## Usage

```python
from geometry import *

# create a shape
circle = Circle(radius = 5)
# get area
print(circle.area())

# get area stats
print(area_stats(circle))
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)