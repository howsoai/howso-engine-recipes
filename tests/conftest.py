import os
from pathlib import Path
import pytest
from testbook import testbook


@pytest.fixture(scope="module")
def tb(request):  # noqa: C901
    cwd = os.getcwd()

    # Search the directory for the notebook filepath
    filename_to_find = request.module.tb_filename

    def find_file(filename, search_path):
        for root, _, files in os.walk(search_path):
            if filename in files:
                return os.path.relpath(os.path.join(root, filename), start=search_path)
        return None

    file_path = find_file(filename_to_find, cwd)
    if file_path:
        notebook_directory = Path(find_file(filename_to_find, cwd)).parent
    else:
        notebook_directory = None
        print(f"WARNING: File {filename_to_find} does not exist.")

    if notebook_directory:
        try:
            os.chdir(notebook_directory)
        except Exception as exc:
            print(
                f'WARNING: There was an issue changing the working '
                f'directory to "{notebook_directory}". ({exc})')

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
