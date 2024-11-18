## To do a new release

- Update `pyproject.toml`, in particular the `version`, `dependencies` and `requires-python`.
- Run `pdm lock` to create an environment with these contraints.
- Run `pdm install && pdm bundle` to test creation of the standalone executable.
- If `requires-python` has changes, update `python-version` in the CI rule `.github/workflows/build_on_several_platforms.yaml`.
- Run the CI by opening a PR and merging the commit on `main`.
- Create a new Github release. Artifact should be uploaded automatically.
