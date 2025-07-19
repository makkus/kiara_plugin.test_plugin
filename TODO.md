# Tasks for the 'test_plugin' kiara plugin

This file contains open (and completed) tasks for this project

### Todo

- [ ] enable Github Pages on your repository
  - wait for the first 'build latest docs' action to finish: https://github.com/makkus/kiara_plugin.test_plugin/actions
  - go to: https://github.com/makkus/kiara_plugin.test_plugin/settings/pages
  - go to the 'Pages' sub-section
  - choose the `gh-pages` branch
  - leeve the `/root` path setting
  - click 'Save'
  - wait for the `pages build and deployment' action to finish (again, under the 'Actions' tab)
  - go to: https://makkus.github.io/kiara_plugin.test_plugin/latest
  - check that the documentation is there
  - the root-level documentation page will not work yet, but will be fixed after you release the first version of your plugin:
    - https://makkus.github.io/kiara_plugin.test_plugin
- [ ] create [trusted publisher](https://docs.pypi.org/trusted-publishers/) on https://pypi.org/manage/account/publishing/
  - settings to use:
    - `PyPI Project Name`: `kiara_plugin.test_plugin`
    - `Owner`: `makkus`
    - `Repository name`: `kiara_plugin.test_plugin`
    - `Workflow name`: `build-linux.yaml`
    - `Environment name`: [leave empty]
- [ ] configure conda package publishing
    - [ ] create an account on https://anaconda.org (if necessary)
    - [ ] create API token to allow Github actions to push to anaconda: https://anaconda.org/freckles/settings/access
      - settings to use:
        - `Token Name`: choose anything, maybe `kiara_plugin.test_plugin Github Action`
        - `Strength`: Strong
        - `Scopes`:
          - `Allow write access to the API site`
        - `Expiration date`: choose whatever you deem sensible
    - [ ] create new repository secret at: https://github.com/makkus/kiara_plugin.test_plugin/settings/secrets/actions
        - `Name`: `ANACONDA_PUSH_TOKEN`
        - `Secret`: the token you created above

- [ ] examine and run example module (and module config)
  - [`src/kiara_plugin/test_plugin/modules/__init__.py`](https://github.com/makkus/kiara_plugin.test_plugin/blob/develop/src/kiara_plugin/test_plugin/modules/__init__.py)
      - run it via: `uv run kiara run test_plugin.example text_1="Hello" text_2="World"`
  - [`examples/jobs/example_job_test_plugin.yaml`](https://github.com/makkus/kiara_plugin.test_plugin/blob/develop/examples/jobs/example_job_test_plugin.yaml) (which uses this [pipeline](https://github.com/makkus/kiara_plugin.test_plugin/blob/develop/examples/pipelines/example_pipeline_test_plugin.yaml))
      - run it via: `uv run kiara run examples/jobs/example_job_test_plugin.yaml`
- [ ] delete example module and job:
  - once you have confirmed everything works, delete the `ExampleModule` that comes with this template, along with everything related:
    - `src/kiara_plugin/test_plugin/modules/__init__.py`:
        - the `ExampleModuleConfig` class
        - the `ExampleModule` class
    - `examples/jobs/example_job_test_plugin.yaml`
    - `examples/pipelines/example_pipeline_test_plugin.yaml`
- [ ] start writing your own modules!

### In Progress

- [ ] create remote git repository on https://github.com/new:
  - settings to use:
    - `Owner`: `makkus`
    - `Repository name`: `kiara_plugin.test_plugin`
    - `Description`: `A plugin.`
- [ ] add the Github repository as remote:
  - `git remote add origin git@github.com:makkus/kiara_plugin.test_plugin.git`
    or:
    `git remote add origin https://github.com/makkus/kiara_plugin.test_plugin.git`
- [ ] push the initial version:
  - `git push --set-upstream origin develop`
  - now visit the Github Actions tab in your new repo and check that the pre-configured actions all run without error:
    - https://github.com/makkus/kiara_plugin.test_plugin/actions

### Done

- [x] create project directory structure
- [x] create local git repository
