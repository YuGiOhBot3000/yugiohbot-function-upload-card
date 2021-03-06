from google.cloud import storage


def download_image(file):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('generated-cards')
    blob = bucket.blob(file)

    blob.download_to_filename('/tmp/' + file)
    print('Blob {} downloaded.'.format(file))
