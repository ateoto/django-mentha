#!/usr/bin/env python
import sys

import django
from django.conf import settings


if not settings.configured:
    from mentha.tests import test_settings
    settings.configure(**test_settings.__dict__)


def runtests(*test_args):
    if hasattr(django, 'setup'):
        django.setup()

    from django.test.utils import get_runner

    apps = sys.argv[1:] or ['mentha', ]
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=2, interactive=True)
    failures = test_runner.run_tests(apps)
    sys.exit(failures)

if __name__ == '__main__':
    runtests(*sys.argv[1:])
