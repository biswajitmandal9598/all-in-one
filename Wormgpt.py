try:
    import requests
except ModuleNotFoundError:
    import os
    os.system("pip install requests")
a = f"""\033[0m

 __      __                        _____________________________
/  \    /  \___________  _____    /  _____/\______   \__    ___/
\   \/\/   /  _ \_  __ \/     \  /   \  ___ |     ___/ |    |   
 \        (  <_> )  | \/  Y Y  \ \    \_\  \|    |     |    |   
  \__/\  / \____/|__|  |__|_|  /  \______  /|____|     |____|   
       \/                    \/          \/                     

Welcome To Worm GPT , The Biggest Enemy of Chat Gpt. By all info gather telegram : @biswa_yt

"""
print(a)


while True:
    mode = "wormgpt"

    user_message = input("- Entre your msg: ")

    if user_message == 'exit' or user_message == 'exit()':
        exit("\nThe conversation has ended ")
    url = "https://dev-loopgpt.pantheonsite.io/wp-admin/js/loop/WormGpt.php?prompt=" + str(
        user_message) + "&" + "model=" + str(mode) + "&pass=" + str(len(a))

    response = requests.get(url).text

    print("\n-" + str(response) + "\n")

