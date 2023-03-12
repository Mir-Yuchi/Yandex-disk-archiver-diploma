import requests
from app.keys import VK_TOKEN, VK_VERSION


class PlusFunction:

    @staticmethod
    def upload_by_url(is_token, path, url):
        resources = 'https://cloud-api.yandex.net/v1/disk/resources/'
        basic_header = {"Authorization": f"OAuth {is_token}"}
        response = requests.post(
            resources + "upload",
            headers=basic_header,
            params={"path": path, "url": url}
        )
        match response.status_code:
            case 202:
                print("Success uploaded")
            case 409:
                print("File with similar name already exists!")
            case _:
                print("Something went wrong... Please try again!")
        return response.status_code

    @staticmethod
    def from_vk(is_token):
        domain = input("Enter VK id or username --> ")
        res = requests.get('https://api.vk.com/method/wall.get',
                           params={
                               'access_token': VK_TOKEN,
                               'v': VK_VERSION,
                               'domain': domain
                           }).json()
        total = res['response']['count']
        print(f"Total posts: {total} \U0001F4D1")
        number = input("Enter number of posts you want to archive --> ")
        if int(number) > total:
            print("You entered more posts than you have")
            return PlusFunction.from_vk(is_token)
        folder = input("\n\tChoose option: \n"
                       "\t1 - Upload to existing folder \U0001F4C1 \n"
                       "\t2 - Use default folder  \U0001F4C1 \n")
        folder_name: str
        match folder:
            case "1":
                folder_name = input("Enter folder name --> ")
            case "2":
                folder_name = "images_from_vk"
                requests.put(f"https://cloud-api.yandex.net/v1/disk/resources/?path=%2F{folder_name}",
                             headers={'Authorization': f'OAuth {is_token}'}).json()
            case _:
                print("Wrong option \U0001F6AB")
                return PlusFunction.from_vk(is_token)
        for photos in res['response']['items']:
            for photo in photos['attachments']:
                if photo['type'] == 'photo':
                    name = f"/{folder_name}/photo.jpg"
                    url = photo['photo']['sizes'][-1]['url']
                    PlusFunction.upload_by_url(is_token, name, url)

    @staticmethod
    def manually(is_token):
        url = input("Enter url --> ")
        folder = input("\n\tChoose option: \n"
                       "\t1 - Upload to existing folder \U0001F4C1 \n"
                       "\t2 - Use default folder  \U0001F4C1 \n")
        folder_name: str
        match folder:
            case "1":
                folder_name = input("Enter folder name --> ")
            case "2":
                folder_name = "manually_passed"
                requests.put(f"https://cloud-api.yandex.net/v1/disk/resources/?path=%2F{folder_name}",
                             headers={'Authorization': f'OAuth {is_token}'}).json()
            case _:
                print("Wrong option \U0001F6AB")
                return PlusFunction.manually(is_token)
        name = f"/{folder_name}/photo.jpg"
        PlusFunction.upload_by_url(is_token, name, url)
