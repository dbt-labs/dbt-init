## Releasing
1. In a virtual env, install package via: `python setup.py install`. Check that
it works
2. Clear out the `dist/` folder
3. Bump the version number in setup.py
4. `python setup.py bdist_wheel` -- check that the right starter project files
were included
5. `twine upload dist/*`
