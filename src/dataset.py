# dataset.py: Starter file
import kagglehub
import shutil

# Download latest version (code from kaggle)
def import_raw_data(kaggleset="samfenske/euro-resistance"):
    path = kagglehub.dataset_download(kaggleset)
    print("Original path to dataset files:", path)

    shutil.move(path, "data/raw")
    print("Dataset moved to data/raw folder successfully")

if __name__ == "__main__":
    import_raw_data()