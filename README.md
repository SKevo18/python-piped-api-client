# Python project template

A template for new Python projects.

## Features

- Automatically builds [PDoc](https://pdoc3.github.io/pdoc/) documentation & uploads package to [PyPI](https://pypi.org) on new GitHub release, thanks to GitHub actions;
- Tests with pyTest before uploading to PyPI (or you can test manually with `workflow-dispatch`);
- Ready-to-go `setup.py` file;
- Scripts to build documentation and compile as a Python package;
- A to-do list below;
- Possibly more ;)

## Your to-do list

(*Approx. time to set up:* 15 - 25 minutes)

- [ ] Edit `# FIXME` lines to match your project;
  - [ ] setup.py
    - [ ] Package name
    - [ ] License
    - [ ] Version
    - [ ] Author
    - [ ] Author email
    - [ ] Description
    - [ ] Keywords
    - [ ] Classifiers
    - [ ] Repository URL
- [ ] Setup virtualenv (`scripts/setup_virtualenv_windows.ps1` for Windows);
- [ ] Rename `python_project_template` folder and start writing your source code;
- [ ] Add your dependencies to `requirements.txt`;
- [ ] Update .gitingore with your stuff;
- [ ] Replace this `README.md` file with a fancier one;
- [ ] Upload code to your GitHub repository;
- [ ] Turn on GitHub pages and use `documentation` as your pages branch;
- [ ] Add your editior to `.gitignore`;
- [ ] Add your PyPI API key to GitHub secrets (`PYPI_API_TOKEN`);
- [ ] When your are done, make a new release at GitHub to build documentation and upload to PyPI;
  - Don't forget to bump version in `setup.py` everytime you do a new release!!!

That should be it. Happy coding!

If you have any questions or found a bug, please open a new issue in this repository.

## 🎁 Support me

I create free software to benefit people.
If this project helps you and you like it, consider supporting me by donating via cryptocurrency:

- Bitcoin: `bc1q6n7f4mllak9xts355wlyq2n3rce60w2r5aswxa`; `1LMS4u41beDGMb9AXmXzfH7ZkZSwGSkSyx`
- Ethereum: `0x12C598b3bC084710507c9d6d19C9434fD26864Cc`
- Litecoin: `LgHQK1NQrRQ56AKvVtSxMubqbjSWh7DTD2`
- Dash: `Xe7TYoRCYPdZyiQYDjgzCGxR5juPWV8PgZ`
- Zcash: `t1Pesobv3SShMHGfrZWe926nsnBo2pyqN3f`
- Dogecoin: `DALxrKSbcCXz619QqLj9qKXFnTp8u2cS12`
- Ripple: `rNQsgQvMbbBAd957XyDeNudA4jLH1ANERL`
- Monero: `48TfTddnpgnKBn13MdJNJwHfxDwwGngPgL3v6bNSTwGaXveeaUWzJcMUVrbWUyDSyPDwEJVoup2gmDuskkcFuNG99zatYFS`
- Bitcoin Cash: `qzx6pqzcltm7ely24wnhpzp65r8ltrqgeuevtrsj9n`
- Ethereum Classic: `0x383Dc3B83afBD66b4a5e64511525FbFeb2C023Db`

More cryptocurrencies are supported. If you are interested in donating with a different one, please [E-mail me](mailto:me@kevo.link).
No other forms of donation are currently supported.
