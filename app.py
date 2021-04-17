from os import system, listdir
from os.path import isfile, join

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
import tkinter.messagebox as messagebox

import json
import time

import logger_class


# noinspection PyBroadException
class App:
    # region Main Window Attributes

    mainWindow = None
    listboxSavedProfiles = None

    # endregion

    # region Class Variables

    profilesNames = []
    profilesDirPath = 'profiles/'
    __errorClass = 'app_error'
    __error = None

    # endregion

    def launchApplication(self):
        self.initializeMainWindow()
        self.mainWindow.mainloop()

    # region Main Window

    # region Main Window Initialization Methods

    def initializeMainWindow(self):
        try:
            self.createMainWindowGUI()
        except:
            print("Main window initialization error")
            self.__error = '[AP#C1]MAIN_INIT_ERROR'
            lg = logger_class.Logger().logError(self.__errorClass, self.__error)
            if not lg: print("Error has not been logged")
            del lg

        try:
            self.createMainWindowButtons()
        except AttributeError:
            print("Button function not recognized")
            self.__error = '[AP#C2]BUTTONS_INIT_ERROR'
            lg = logger_class.Logger().logError(self.__errorClass, self.__error)
            if not lg: print("Error has not been logged")
            del lg

        try:
            self.createMainWindowListbox()
        except AttributeError:
            print("List box items not found")
            self.__error = '[AP#C3]LISTBOX_INIT_ERROR'
            lg = logger_class.Logger().logError(self.__errorClass, self.__error)
            if not lg: print("Error has not been logged")
            del lg

        try:
            self.loadProfiles()
        except:
            print("Error while loading profiles")
            self.__error = '[AP#C4]PROFILES_LOADING_ERROR'
            lg = logger_class.Logger().logError(self.__errorClass, self.__error)
            if not lg: print("Error has not been logged")
            del lg

    # region Main Window Components Creation

    def createMainWindowGUI(self):
        self.mainWindow = Tk()
        self.mainWindow.geometry('380x200')
        self.mainWindow.title('Virtual Windows Manager')
        self.mainWindow.resizable(0, 0)

    def createMainWindowButtons(self):
        buttonCreateProfile = Button(self.mainWindow, text='Create Profile', width=15, font=('Arial', 10),
                                     command=self.createProfile)
        buttonEditProfile = Button(self.mainWindow, text='Edit Profile', width=15, font=('Arial', 10),
                                   command=self.editProfile)
        buttonDeleteProfile = Button(self.mainWindow, text='Delete Profile', width=15, font=('Arial', 10),
                                     command=self.deleteProfile)
        buttonLaunchProfile = Button(self.mainWindow, text='Launch Profile', width=15, font=('Arial', 10),
                                     command=self.launchProfile)

        buttonCreateProfile.place(x=15, y=20)
        buttonEditProfile.place(x=15, y=60)
        buttonDeleteProfile.place(x=15, y=100)
        buttonLaunchProfile.place(x=15, y=140)

    def createMainWindowListbox(self):
        self.listboxSavedProfiles = tk.Listbox(self.mainWindow, width=35)
        self.listboxSavedProfiles.insert(0, *self.profilesNames)

        self.listboxSavedProfiles.place(x=160, y=20)

    # endregion

    # region Main Window Components Updating

    def loadProfiles(self):
        try:
            listdir(self.profilesDirPath)
        except FileNotFoundError:
            system('cmd /c "mkdir profiles"')
            system('cmd /c "echo.>profiles.txt"')

        try:
            self.updateProfilesFile()
            self.updateProfilesList()

        except ValueError:
            self.createProfilesFile()
            self.updateProfilesList()

        print(self.profilesNames)

    def updateProfilesFile(self):
        savedProfileFiles = [f.replace('.json', '') for f in listdir(self.profilesDirPath) if
                             isfile(join(self.profilesDirPath, f))]
        savedProfileFiles.remove('profiles.txt')
        profiles = open('profiles/profiles.txt', 'r')
        profileNames = [profilesName.strip('\n') for profilesName in profiles.readlines()]
        profileNames = [profileName.replace(' ', '').lower() for profileName in profileNames]

        for fileName in savedProfileFiles:
            if fileName.replace(' ', '').lower() not in profileNames:
                open('profiles/profiles.txt', 'a').write(fileName + '\n')

        profiles.close()

    def updateProfilesList(self):
        self.profilesNames = [name.strip('\n') for name in open('profiles/profiles.txt', 'r').readlines()]

    def createProfilesFile(self):
        system('cmd /c "echo.>profiles/profiles.txt"')
        savedProfileFiles = [f.replace('.json', '') for f in listdir(self.profilesDirPath) if
                             isfile(join(self.profilesDirPath, f))]
        savedProfileFiles.remove('profiles.txt')

        open('profiles/profiles.txt', 'a').writelines(savedProfileFiles)

    # endregion

    # endregion

    # region Main Window Button Methods

    def createProfile(self):
        pass

    def editProfile(self):
        pass

    def deleteProfile(self):
        pass

    def launchProfile(self):
        pass

    # endregion

    # endregion


App().launchApplication()
