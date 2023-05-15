# napari-indices

[![License BSD-3](https://img.shields.io/pypi/l/napari-indices.svg?color=green)](https://github.com/Emmanulla0/napari-indices/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-indices.svg?color=green)](https://pypi.org/project/napari-indices)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-indices.svg?color=green)](https://python.org)
[![tests](https://github.com/Emmanulla0/napari-indices/workflows/tests/badge.svg)](https://github.com/Emmanulla0/napari-indices/actions)
[![codecov](https://codecov.io/gh/Emmanulla0/napari-indices/branch/main/graph/badge.svg)](https://codecov.io/gh/Emmanulla0/napari-indices)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-indices)](https://napari-hub.org/plugins/napari-indices)

Calculer les indices de végétation

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-indices` via [pip]:

    pip install napari-indices



To install latest development version :

    pip install git+https://github.com/Emmanulla0/napari-indices.git

## Plugin description


After programming the plugin, it was installed and launched by accessing the Plugins menu > Napari-vegetation-indices-fisher-ratio > Vegetation indices. Using the plugin requires importing the bands of a hyperspectral image. Then, the vegetation index to be calculated and the desired bands to use must be selected. Finally, clicking the **Run** button initiates the calculation.

To define the regions of interest for analysis, click on the Shapes button in the Napari interface and choose the **add rectangle** option from the menu that appears. Using the mouse, draw a rectangle around each of the two areas to be analyzed, for example, a tree leaf and a green paper leaf.

To calculate the Fisher ratio and display the histogram, go back to the Plugins menu > Napari-vegetation-indices-fisher-ratio > ExampleGWidget and click the **Click me!** button. This action opens a new window displaying the optimal vegetation index to use, its corresponding Fisher ratio, and the histogram of the two selected regions on the vegetation index image.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-indices" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/Emmanulla0/napari-indices/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
