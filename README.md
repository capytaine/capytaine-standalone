# Capytaine standalone distribution

This repository stores the recipe to bundle a full Python distribution with [Capytaine](https://github.com/capytaine/capytaine) into a single file executable file.

## Download

Choose the file corresponding to your OS in the ["Release" section of the Github page](https://github.com/capytaine/capytaine-standalone/releases).

After downloading the file, you might need to give it permission to be executed as a program. On Linux, the command is as follows:
```shell
chmod +x ipython-with-capytaine-linux
```

## Usage

In a terminal, use the following command to open an [IPython shell](https://ipython.readthedocs.io/en/stable/) with Capytaine pre-loaded:
```shell
./ipython-with-capytaine-linux
```
In this shell, you can run any Python command, including commands using Capytaine:
```python
In [1]: print("Hello world")
Hello world

In [2]: mesh = cpt.mesh_sphere()
Out[2]: Mesh(vertices=[[... 92 vertices ...]], faces=[[... 100 faces ...]], name="sphere_0")
```

To execute a whole Python script, you can pass it as argument to the command line
```shell
./ipython-with-capytaine-linux radiation_cylinder.py
```
or, from within the IPython shell, use the following "magic" command:
```python
In [3]: %run radiation_cylinder.py
```


## Limitations

- Interactive display of Matplotlib plots (`plt.show()`) seems to be broken. But saving the plot to a file (`plt.savefig('example.pdf')`) works.

- You cannot install other Python libraries in the bundled environment. If you have specific need, you will need to use `pip` or `conda` to install Capytaine in a virtual environment that you can customize.

- On MacOS, the standalone version is only built for the ARM architecture (Apple Silicon processors), since Capytaine 2.2. Packages for the legacy MacOS Intel architecture are still available on `pip` or `conda`.

## Support

Please report issues to [Capytaine's main issue tracker](https://github.com/capytaine/capytaine/issues) while mentionning `[capytaine-standalone]` in the issue title.
