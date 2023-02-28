import requests
import math
from app.disk import run


def convert_size(size_bytes):  # bite converter
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


class Function:
    def __init__(self):
        pass

    @staticmethod
    def get_user_json(token):
        response = requests.get('https://cloud-api.yandex.net/v1/disk', headers={'Authorization': f'OAuth {token}'})
        return response.json()

    @staticmethod
    def get_user_info(token):
        response = requests.get('https://cloud-api.yandex.net/v1/disk', headers={'Authorization': f'OAuth {token}'})
        info = response.json()
        print("Total space  \U0001F4E6: ", convert_size(info['total_space']),
              "\nUsed space \U0001F5F3: ", convert_size(info["used_space"]),
              "\nTrash size\U0001F5D1: ", convert_size(info['trash_size']), "\n",
              50 * "-", "\n")

    @staticmethod
    def get_files_folders(token):
        resources = 'https://cloud-api.yandex.net/v1/disk/resources/'
        next_choice = input("\t\t\tChoose option \U0001F447"
                            "\n\t 1 - Create a folder \U0001F4C2"
                            "\n\t 2 - Deleting files \U0001F6AE"
                            "\n\t 3 - Get a link to download files \U0001F4E5"
                            "\n\t 4 - Get a link to upload files \U0001F4E4"
                            "\n\t 5 - Upload files to disk by URL \U0001F4E4 \U0001F4E5 "
                            "\n\t 6 - Back to the main menu \U0001F519 \n")
        match next_choice:
            case '1':
                path = input("Enter name: ")
                files = requests.put(resources + f"?path=%2F{path}",
                                     headers={'Authorization': f'OAuth {token}'}).json()
                if 'description' in files:
                    print(files['description'])
                else:
                    print("Folder successfully created :)")
            case '2':
                path = input("  Enter name: ")
                requests.delete(resources + f"?path=%2F{path}",
                                headers={'Authorization': f'OAuth {token}'})
                print("Successfully deleted :)")
            case '3':
                path = input("Enter path\U000023E9: ")
                download = requests.get(resources + f"download?path=%2F{path}",
                                        headers={'Authorization': f'OAuth {token}'}).json()
                if 'description' in download:
                    print(download['description'])
                else:
                    print("Cath the link dude -> ", download["href"])
            case '4':
                path = input("Enter path\U000023E9: ")
                upload = requests.get(resources + f"upload?path=%2F{path}",
                                      headers={'Authorization': f'OAuth {token}'}).json()
                if 'description' in upload:
                    print(upload['description'])
                else:
                    print("Cath the link dude -> ", upload["href"])
            case '5':
                url = input("Enter URL\U0001F517: ")
                path = input("Enter PATH\U000023E9: ")
                publish = requests.post(resources + f"upload?url={url}&path=%2F{path}",
                                        headers={'Authorization': f'OAuth {token}'}).json()
                if 'description' in publish:
                    print(publish['description'])
                else:
                    print("Successfully downloaded :)")
            case '6':
                return run.app(token)
            case _:
                print("Wrong choice \U0001F61E")
                return Function.get_files_folders(token)

    @staticmethod
    def public_files_and_folders(token):
        next_choice = input("\t\t\tChoose option \U0001F447"
                            "\n\t 1 - Get meta information about public file in catalog  \U00002139"
                            "\n\t 2 - Get a link to download a public resource \U0001F517"
                            "\n\t 3 - Save the public resource to the Downloads folder \U0001F4BE \n"
                            "\n\t 4 - Back to the main menu \U0001F519 \n")
        match next_choice:
            case '1':
                path = input("Enter public key url \U000023E9: ")
                response = requests.get("https://cloud-api.yandex.net/v1/disk/public/resources?public_key=" + path,
                                        headers={'Authorization': f'OAuth {token}'}).json()
                total_items = response['_embedded']['total']
                print("Total items: ", total_items, 50 * "-", "\n")
                if total_items == 0:
                    print("No items in catalog")
                else:
                    for item in response['_embedded']['items']:
                        print("Name: ", item['name'], "\nType: ", item['type'], "\nSize: ", convert_size(item['size']),
                              "\nMedia type:", item['media_type'], "\n", 50 * "-", "\n")
            case '2':
                path = input("Enter public key url \U000023E9: ")
                response = requests.get(
                    "https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key=" + path,
                    headers={'Authorization': f'OAuth {token}'}).json()
                print("Cath the link dude ---> ", response['href'])
            case '3':
                path = input("Enter public key url \U000023E9: ")
                requests.post(
                    "https://cloud-api.yandex.net/v1/disk/public/resources/save-to-disk?public_key=" + path,
                    headers={'Authorization': f'OAuth {token}'}).json()
                print("Successfully downloaded :)")
            case '4':
                return run.app(token)
            case _:
                print("Wrong choice \U0001F61E")
                return Function.public_files_and_folders(token)

    @staticmethod
    def trash_func(token):
        next_choice = input("\t1 - Trash Delete\U0000267B \n"
                            "\t2 - Get trash container \U0001F5D1 \n"
                            "\t3 - Trash Restore\U0001F5D1 \n"
                            "\t4 - Back to the main menu \U0001F519 \n")
        match next_choice:
            case '1':
                requests.delete("https://cloud-api.yandex.net/v1/disk/trash/resources",
                                headers={'Authorization': f'OAuth {token}'}).json()
                print("Trash Successfully deleted\U00002705")
            case '2':
                response = requests.get("https://cloud-api.yandex.net/v1/disk/trash/resources?path=%2F",
                                        headers={'Authorization': f'OAuth {token}'}).json()
                total_items = response['_embedded']['total']
                print("Total items: ", total_items, '\n', 50 * "-", "\n")
                if total_items == 0:
                    print("No items in catalog")
                else:
                    for item in response['_embedded']['items']:
                        print("Name: ", item['name'], "|| Path --> ", item['path'],
                              "\n", 50 * "-", "\n")
            case '3':
                path = input("Enter path\U000023E9: ")
                response = requests.put("https://cloud-api.yandex.net/v1/disk/trash/resources/restore?path=%2F" + path,
                                        headers={'Authorization': f'OAuth {token}'}).json()
                if 'description' in response:
                    print(response['description'])
                else:
                    print("Successfully restored \U00002705")
            case '4':
                return run.app(token)
            case _:
                print("Wrong choice \U0001F61E")
                return Function.trash_func(token)
