import os
import zipfile
import shutil


def zip_file(folder_path_transit, folder_path_model_webgl):
    print("fichier ouvert")

    extensionBin = ".bin"

    # adresse où va arriver ton export 3dsmax
    # RepoTransit = "F:/infographie/dev/autoZip/transit/"
    RepoTransit = "{}".format(folder_path_transit)
    # adresse de là où tu mets ton zip pour le webgl
    # ModelWebgl = "F:/infographie/dev/autoZip/target/"
    ModelWebgl = "{}".format(folder_path_model_webgl)
    # adresse où tu vas sauvegarder une copie de ton ZIP
    SaveDirectory = "F:/infographie/dev/autoZip/target_save/"

    # detecte tout les fichiers dans le dossier et les mets dans une liste
    listeFichier = os.listdir(RepoTransit)

    # recherche le fichier avec la bonne extension pour capturer son nom de fichier
    for listEntry in listeFichier:
        if listEntry.endswith(extensionBin):
            finalNameFile = listEntry.replace(extensionBin, "")
            finalName_ZIP = finalNameFile + ".zip"
            # print(listEntry)
            # print(finalNameZIP)

    print(finalName_ZIP)

    # Creation du fichier zip avec le nom capturé au dessus
    myZipfile = zipfile.ZipFile("{}{}".format(RepoTransit, finalName_ZIP), mode='w', compression=zipfile.ZIP_DEFLATED)


    # Introduction des fichiers qui sont présents dans le directory à lintérieur du fichier zip
    for fichier2Save in listeFichier:
        print(fichier2Save, "zipped in file")
        myZipfile.write("{0}{1}".format(RepoTransit, fichier2Save), arcname=fichier2Save)

    myZipfile.close()

    print("--------------------------")

    # efface les fichiers qui ont servis à creer le zip afin de nettoyer le directory
    # for fichier2Save in listeFichier:
    #     print(fichier2Save, "cleaned from base directory")
    #     os.remove("U:/Sandbox/Andrei/python_script/test/{0}".format(fichier2Save))

    # Bouge le fichier zip dans sa location final et dans un dossier de sauvegarde
    shutil.copy("{}{}".format(RepoTransit, finalName_ZIP), SaveDirectory)
    shutil.move("{}{}".format(RepoTransit, finalName_ZIP), ModelWebgl)