import zipfile
import pathlib
import requests
import click
import shutil

movie_lens_url = (
    "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
)
dataset_dir_name = "ml-latest-small"


def download_movie_lens(
    temp_dir: pathlib.Path, clear_cache: bool = False
) -> pathlib.Path:
    if not temp_dir.is_dir():
        temp_dir.mkdir(parents=True)
    dest = temp_dir / "movielens.zip"
    if dest.is_file() and not clear_cache:
        print(f"Skipping download - using cached dataset at {dest}")
    else:
        r = requests.get(movie_lens_url, stream=True)
        if r.status_code == 200:
            print("Downloading MovieLens...")
            with dest.open("wb") as binary_zip:
                shutil.copyfileobj(r.raw, binary_zip)
            print(f"Downloaded MovieLens to {dest}")
        else:
            print(f"Error: download reported status code {r.status_code}")
    return dest


def extract_dataset(src: pathlib.Path, dest: pathlib.Path, force=False) -> None:
    dataset_loc = dest / dataset_dir_name
    if dataset_loc.is_dir() and not force:
        print(f"Skipping extraction - using dataset at {dataset_loc}")
    else:
        with zipfile.ZipFile(src, "r") as zipped:
            print("Extracting MovieLens...")
            zipped.extractall(dest)
        print(f"Extracted MovieLens to {dest}")


def clean_dir(dir: pathlib.Path) -> None:
    temp_dir = dir / "temp"
    dataset_loc = dir / dataset_dir_name
    print("Removing cached data...", end="")
    for file in temp_dir.iterdir():
        file.unlink()
    temp_dir.rmdir()
    print("DONE")
    print("Removing dataset...", end="...")
    for file in dataset_loc.iterdir():
        file.unlink()
    dataset_loc.rmdir()
    print("DONE")
    print("Removing any other files...", end="")
    for file in dir.iterdir():
        file.unlink()
    print("DONE")


@click.command()
@click.option(
    "-o",
    "--output",
    "data_dirpath",
    help="Specifies directory to write dataset to.",
    type=str,
    default="./data/",
    show_default=True,
)
@click.option(
    "-f",
    "--force",
    help="Forces current action, even if cached data exists.",
    default=False,
    is_flag=True,
)
@click.option(
    "-e",
    "--extract",
    nargs=2,
    help="Extracts specified zipped dataset to specified directory",
    type=str,
    default=None,
)
@click.option(
    "-d",
    "--download",
    help="Downloads new copy of MovieLens100k to the specified directory",
    type=str,
    default=None,
)
@click.option("-c", "--clean", help="Cleans specified data directory.")
def setup_dataset(
    data_dirpath: str, force: bool, extract: str, download: str, clean: str
) -> None:
    if download:
        location = pathlib.Path(download)
        try:
            dataset_loc = download_movie_lens(location, force)
        except FileNotFoundError:
            print(f"Error: Could not write to location at {location}.")
    if extract:
        src, dest = pathlib.Path(extract[0]), pathlib.Path(extract[1])
        try:
            extract_dataset(src, dest, force=force)
        except FileNotFoundError:
            print(
                f"Error: Could not open cached dataset at {src}. Make sure the dataset is downloaded."
            )
    if clean:
        data_dir = pathlib.Path(clean)
        clean_dir(data_dir)
    if not download and not extract and not clean:
        data_dir = pathlib.Path(data_dirpath)
        temp_dir = data_dir / "temp"
        dataset_loc = download_movie_lens(temp_dir, force)
        extract_dataset(dataset_loc, data_dir, force)


if __name__ == "__main__":
    setup_dataset()
