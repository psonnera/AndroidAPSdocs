# Redirect 
These redirect scripts are created to facilitate language split of the projects.

The standard user defined redirects are not capable to redirect into another language or project.
https://docs.readthedocs.io/en/stable/user-defined-redirects.html

We can use the public API to create the redirects.

## Redirects

`/en/latest/CROWDIN/<lang>/*` will be redirected `/cs/latest/*`

Example:

`/en/latest/CROWDIN/cs/index.html` => `/cs/latest/index.html`

## Scripts

### Generate Redirects

Generate a list of redirects. For each page in the CROWDIN folder a redirect is generated and stored in a `redirect.json` file.

``` console
$ python generateRedirects.py
```

### Import Redirects

This script loads the `redirect.json` and calls for each record the readthedocs API
https://docs.readthedocs.io/en/stable/api/v3.html#redirects

Note that the API is limited in throughput and will be throttled, and the script will take some time to complete.

The API token can be generated in the GUI and should be passed as a parameter.
https://docs.readthedocs.io/en/stable/api/v3.html#token

``` console
$ python importRedirects.py <APIKEY>
```

### Import Redirects

This script removes all redirect from the project. The script could be used for testing or maintenance.
**NOTE: this script will remove all redirects, including the ones that are manual added trough the GUI.

``` console
$ python deleteAllRedirects.py <APIKEY>
```

## CROWDIN orphan cleanup

Use this script to remove files that exist in `docs/CROWDIN/<lang>/...` but do not exist in `docs/EN/...` at the same relative path.

- Default mode is dry run and writes a manifest file.
- Use `--markdown-only` to target only `.md` files.
- Use `--apply` to actually delete files (tracked files are removed with `git rm`).

```console
# Dry run, all file types
python utils/prune_crowdin_orphans.py

# Delete all orphan files and prune empty directories
python utils/prune_crowdin_orphans.py --apply --prune-empty-dirs

# Delete only orphan markdown files
python utils/prune_crowdin_orphans.py --apply --markdown-only
```
