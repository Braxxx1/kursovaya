import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        head = {"Content-Type": "application/json", "Authorization": f"OAuth {self.token}"}
        params = {"path": 'neotology_photo_vk/fdss.jpg', 'overwrite':'true'}
        response = requests.get(url=upload_url, headers=head, params=params)
        hr = response.json().get("href")
        response = requests.put(url=hr, data=open(file_path, 'rb'))        


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    
    path_to_file = "images_vk\\40.jpg"
    token = 'y0_AgAAAAANuqblAADLWwAAAADg3_4Fu038DgA9SX67jJlS-FPffzQvkX8'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)