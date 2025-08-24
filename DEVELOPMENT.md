# Development Guide

This document centralizes information useful for developers working on FreeCAD. It links to external resources and describes the layout of this repository.

## Repository layout
- `src/` – source code of the application and workbenches
- `tests/` – unit and integration tests
- `tools/` – helper scripts used during development
- `package/` – packaging recipes for supported platforms
- `cMake/` – CMake modules and build helpers
- `contrib/` – third‑party libraries or data bundled with FreeCAD
- `data/` – sample data and runtime configuration files
- `src/Doc/` – templates and configuration for generating the project documentation

## External documentation
The following resources provide additional background and detailed documentation:

- [Wiki](https://wiki.freecad.org)
- [Developers handbook](https://freecad.github.io/DevelopersHandbook/)
- [Forum](https://forum.freecad.org)
- Platform‑specific build guides: [Linux](https://wiki.freecad.org/Compile_on_Linux), [Windows](https://wiki.freecad.org/Compile_on_Windows), [macOS](https://wiki.freecad.org/Compile_on_MacOS), [MinGW](https://wiki.freecad.org/Compile_on_MinGW)

## Development workflow
- Review [CONTRIBUTING.md](CONTRIBUTING.md) for contribution rules and code style expectations.
- Use `pre-commit` to run linters before committing changes. The configuration in `.pre-commit-config.yaml` covers the entire tree.

## Managing TODOs
To keep track of pending work, use the following pattern in code comments:

```
// TODO(#<issue-number>): description
```

Every TODO should reference a GitHub issue describing the task. A pre-commit hook warns about TODOs without a linked issue.

## Packaging and internal tools
Packaging scripts live under [`package/`](package/); tooling for development is under [`tools/`](tools/). See the READMEs in those directories for details.

