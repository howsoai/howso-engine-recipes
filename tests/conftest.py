import os
import pytest

from testbook import testbook


@pytest.fixture(scope="module")
def tb(request):

    cwd = os.getcwd()
    try:
        os.chdir(request.module.tb_dir)
    except AttributeError:
        pass
    except Exception as exc:
        print(f'WARNING: There was an issue changing the working '
              f'directory to "{request.module.tb_dir}". ({exc})')

    execute = True
    try:
        execute = request.module.tb_execute
    except AttributeError:
        pass

    with testbook(request.module.tb_filename, timeout=3600, execute=execute) as tb:
        try:
            if request.module.tb_inject:
                tb.inject(request.module.tb_inject)
        except AttributeError:
            pass

        # https://stackoverflow.com/questions/27071524/python-context-manager-not-cleaning-up
        try:
            yield tb
        finally:
            os.chdir(cwd)


# This is here so that we emit the currently used Amalgam version for direct.
try:
    from howso.client import HowsoClient
    from howso.direct import HowsoDirectClient
    client = HowsoClient()
    if isinstance(client, HowsoDirectClient):
        print(f"Tests appear to be running on direct, the current Amalgam "
              f"version is {client.howso.amlg.get_version_string().decode()}.")
    else:
        print("Tests do not appear to be running on direct.")
except Exception:
    pass
