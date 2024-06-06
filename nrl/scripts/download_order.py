class PhotoDownloader:
    def __init__(self, chat_id):
        self.chat_id = chat_id

    async def download_photo(id, file_path):
        with open(f"orders/{id}.jpg", "wb") as photo_file:
            photo_file.write(file_path.read())

        return "Фотография сохранена."
