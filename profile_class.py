import json
import os

import logger_class
import application_class


class Profile:
    applicationsList = []
    profileDictionary = {}
    __errorClass = 'profile_error'
    __error = None

    def createProfile(self, profileName, profileApplicationsList):
        if self.isProfileValid(profileName, profileApplicationsList):
            self.createProfileDictionary(profileName, profileApplicationsList)
            self.saveProfileData(profileName)
        else:
            print("Profile Creation Error")

        # validate each app

    def __isProfileNameValid(self, name):
        if type(name) is not str:
            self.__error = '[PF#C1]PROFILE_NAME_DATA_TYPE_ERROR'
            lg = logger_class.Logger().logError(self.__errorClass, self.__error)
            if not lg: print("Error has not been logged")
            del lg
            return False
        if len(name) > 16:
            self.__error = '[PF#1]PROFILE_NAME_LENGTH_ERROR'
            lg = logger_class.Logger().logError(self.__errorClass, self.__error)
            if not lg: print("Error has not been logged")
            del lg
            return False

        return True

    def __isApplicationsListValid(self, appList):
        if type(appList) is not list:
            self.__error = '[PF#C2]APP_LIST_DATA_TYPE_ERROR'
            lg = logger_class.Logger().logError(self.__errorClass, self.__error)
            if not lg: print("Error has not been logged")
            del lg
            return False

        for app in appList:
            if type(app) is not dict:
                self.__error = '[PF#C3]APP_DATA_TYPE_ERROR'
                lg = logger_class.Logger().logError(self.__errorClass, self.__error)
                if not lg: print("Error has not been logged")
                del lg
                return False

            appName = app.get('name')
            appPath = app.get('path')
            appWindowValue = app.get('vwindow')
            tempApp = application_class.Application()
            isValid = tempApp.isApplicationValid(appName, appPath, appWindowValue)
            if not isValid:
                self.__error = '[PF#C4]APP_LIST_VALIDATION_ERROR'
                lg = logger_class.Logger().logError(self.__errorClass, self.__error)
                if not lg: print("Error has not been logged")
                del lg
                return False

        return True

    def isProfileValid(self, name, appList):
        if self.__isProfileNameValid(name) and self.__isApplicationsListValid(appList):
            return True
        return False

    def createProfileDictionary(self, name, appList):
        self.profileDictionary = {
            "name": name,
            "applications": appList,
        }

    def saveProfileData(self, name):
        try:
            with open('profiles/profiles.txt', 'a') as infile: infile.write(name + '\n')

            profilePath = 'profiles/' + name + '.json'
            profilePath = profilePath.replace(' ', '').lower()

            with open(profilePath, 'w+', encoding='utf-8') as outfile:
                profileData = [self.profileDictionary]
                json.dump(profileData, outfile, ensure_ascii=False, indent=4)
                outfile.close()
        except FileNotFoundError:
            print("Error while saving profile data")

            self.__error = '[PF#C5]CRUCIAL_SAVING_ERROR'
            lg = logger_class.Logger().logError(self.__errorClass, self.__error)
            if not lg: print("Error has not been logged")
            del lg

        except:
            print("Error while saving profile data")

            self.__error = '[PF#C6]UNKNOWN_CRUCIAL_JSON_SAVING_ERROR'
            lg = logger_class.Logger().logError(self.__errorClass, self.__error)
            if not lg: print("Error has not been logged")
            del lg


# app1 = application_class.Application()
# app1.createApplication('app1', 'path1', 1)
#
# app2 = application_class.Application()
# app2.createApplication('app2', 'path2', 2)
#
# applications = [app1.applicationDictionary, app2.applicationDictionary]
#
# profile = Profile()
# profile.createProfile('Studying Profile', applications)
