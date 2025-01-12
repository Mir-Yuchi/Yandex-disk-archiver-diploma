from app.disk import options, addditional_options
import time


def greeting(is_token):
    print("\t\tWelcome", options.Function.get_user_json(is_token)['user']['display_name'], "\U0001F44B")
    print(50 * "-", "\n")


def app(is_token):
    print("\n\t\t\tHere is some options for you \U0001F447 \n",
          "\t1 - Information About User Disk \U0001F4D1"
          "\n\t2 - Files and Folders \U0001F5C2"
          "\n\t3 - Public Files and Folders \U0001F50E"
          "\n\t4 - Trash \U0001F5D1 \n",
          50 * "-", "\n",
          "\n\t\t\tAdditional options \U0001F447 \n",
          "\t5 - Archive from VK \U0001F4E6",
          "\n\t6 - Archive from Instagram \U0001F4E6",
          "\n\t7 - Pass the links manually \U0001F517",
          "\n\t8 - Archive with VK/Instagram together \U0001F4E6 \n",
          50 * "-", "\n",
          "\t0 - Exit \U0001F6AA \n",
          50 * "-", "\n")
    option = input("Choose what option you want to use -> ")
    print(50 * "-", "\n")
    match option:
        case "1":
            options.Function.get_user_info(is_token)
        case "2":
            options.Function.get_files_folders(is_token)
        case "3":
            options.Function.public_files_and_folders(is_token)
        case "4":
            options.Function.trash_func(is_token)
        case "5":
            addditional_options.PlusFunction.from_vk(is_token)
        case "6":
            addditional_options.PlusFunction.from_instagram(is_token)
        case "7":
            addditional_options.PlusFunction.manually(is_token)
        case "8":
            addditional_options.PlusFunction.from_vk_and_instagram(is_token)
        case "0":
            exit()
        case _:
            print("Wrong option \U0001F6AB")
    time.sleep(2)
    return app(is_token)
