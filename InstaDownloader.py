import instaloader
import sys
import os
import re





try:
    url = sys.argv[1]

    #Diretório de download // Download dir
    download_dir = './'

    os.chdir(download_dir)

    #Loader Instance 
    loader = instaloader.Instaloader(
            download_pictures = True,
            download_videos = True,
            download_video_thumbnails = False,
            download_geotags = False,
            download_comments = False,
            save_metadata = False,
            compress_json = False,
            filename_pattern = '{profile}_{mediaid}'

    )


    #Para baixar de contas privadas // To download from private acc
    from getpass import getpass
    username = "username"
    senha = 'pasword'
    loader.login(username, senha)



    #extrair "short_code" da URL // extract "short_code" from URL
    #exemplo: https://www.instagram.com/p/CCfeQV-AssF/ // example: exemplo: https://www.instagram.com/p/CCfeQV-AssF/
    expr = r'\/p\/([^\/]*)/'
    found = re.search(expr, url)


    if found:
        print(expr)
        print("Baixando ", found.group(1), "...")
        post = instaloader.Post.from_shortcode(loader.context, found.group(1))
        loader.download_post(post, ".")

# Deletando todos os arquivos .txt // Deleting all .txt files
    for file in os.listdir(download_dir):
        if file.endswith(".txt"):
            os.remove(file)

except IndexError:
    print(f'Forma de utilização\n{sys.argv[0]} URL\n')
    sys.exit()
