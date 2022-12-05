#! /bin/bash
find -mindepth 2 -type f -name "*.py" -not -path "./utilities/*" -print0 | xargs -0 --replace bash -xc "poetry run python {}"