## Releasing to pypi
1. In a virtual env, install package via: `python setup.py install`. Run a sample
`dbt-init` command to confirm that it works.
2. Clear out the `dist/` folder
3. Bump the version number in setup.py
4. Switch back to your `dbt-init-dev` virtualenv (which has the `twine` and
`wheel` packages installed). Run `python setup.py bdist_wheel` -- check that the
right starter project files were included in the `.whl` file.
5. Run `twine upload dist/*`
