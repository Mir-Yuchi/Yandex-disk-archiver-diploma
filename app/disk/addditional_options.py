from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


class PlusFunction:
    @staticmethod
    def get_id():
        html = input("Give me a link to profile: ")
        return requests.get(html).text

    @staticmethod
    def from_vk(token):
        profile = PlusFunction.get_id()
        soup = BeautifulSoup(profile, "html.parser")
        images = soup.find_all("img", {"class": "MediaGrid__imageSingle"})
        links = []
        for link in images:
            links.append(urljoin(profile, link["src"]))
        if len(links) == 0:
            print("No images found")
        else:
            print("Total images FOUNDED: ", len(links))
        number = input("How many images you wanna download? --> ")
        next_choice = input("Wanna enter path or use default folder? \n 1 - Default \n 2 - Enter path \n")
        resource = "https://cloud-api.yandex.net/v1/disk/resources"
        match next_choice:
            case '1':
                requests.put(resource + f"?path=%2Fimages_from_vk",
                             headers={'Authorization': f'OAuth {token}'}).json()
                for i in range(int(number)):
                    requests.post(
                        resource + f"?upload?url={links[i]}&path=%2Fdisk%2Fimages_from_vk",
                        headers={'Authorization': f'OAuth {token}'}).json()
                print("Successfully downloaded :)")
            case '2':
                url = "https://images.metmuseum.org/CRDImages/aa/original/DT759.jpg"
                path = input("Enter path\U000023E9: ")
                for i in range(int(number)):
                    publish = requests.post("https://cloud-api.yandex.net/v1/disk/resources/upload?path=disk%2FLoxka&url=https%3A%2F%2Fsun9-70.userapi.com%2Fimpg%2FQtybWh0GZvCRMpw04-ZkqVYb6EGBiNJq5xYjsw%2F3hX5AdIRzrY.jpg%3Fsize%3D320x320%26quality%3D95%26sign%3D94632eaf6e9154d39a88fe0ccf91ff9e%26c_uniq_tag%3DQSFec13s-EKDJ5RxidEIs4Z3oQp7q1B82_DXALGRmTk%26type%3Dalbum",
                                            headers={'Authorization': f'OAuth {token}'}).json()
                    if 'description' in publish:
                        print(publish['description'])
                    else:
                        print("Successfully downloaded :)")
                    print(50*"-")
                    print(publish)
                    print(50 * "-")
