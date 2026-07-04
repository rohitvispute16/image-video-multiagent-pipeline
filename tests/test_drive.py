import gdown

url = "https://drive.google.com/drive/folders/1LjPfQljJ71lsA1gKo4ZN-SCHwBfxSyk9"

gdown.download_folder(
    url=url,
    output="test_images",
    quiet=False,
    use_cookies=False,
)

print("Done")