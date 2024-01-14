import os
import os.path
from glob import glob

import pkg_resources
from tutor import hooks


hooks.Filters.ENV_TEMPLATE_ROOTS.add_items(
    [
        pkg_resources.resource_filename("tutormonitoring", "templates"),
    ]
)

hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("monitoring/build", "plugins"),
    ],
)

for path in glob(
    os.path.join(
        pkg_resources.resource_filename("tutormonitoring", "patches"),
        "*",
    )
):
    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))
