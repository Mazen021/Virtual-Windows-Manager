import logger_class


class Application:
    applicationDictionary = {}
    __errorClass = 'app_error'
    __error = None

    def createApplication(self, name, path, vwindow):
        if self.isApplicationValid(name, path, vwindow):
            self.__createApplicationDictionary(name, path, vwindow)
        else:
            print("Application Creation Error")

    def __isNameValid(self, name):
        if type(name) is not str:
            self.__error = '[AP#C1]APP_NAME_TYPE_ERROR'
            lg = logger_class.Logger().logError(self.__errorClass, self.__error)
            if not lg: print("Error has not been logged")
            del lg
            return False
        if len(name) > 16:
            self.__error = '[AP#1]APP_LENGTH_ERROR'
            lg = logger_class.Logger().logError(self.__errorClass, self.__error)
            if not lg: print("Error has not been logged")
            del lg
            return False

        return True

    def __isPathValid(self, path):
        if type(path) is not str:
            self.__error = '[AP#C2]PATH_TYPE_ERROR'
            lg = logger_class.Logger().logError(self.__errorClass, self.__error)
            if not lg: print("Error has not been logged")
            del lg
            return False
        if len(path) > 128:
            self.__error = '[AP#2]PATH_LENGTH_ERROR'
            lg = logger_class.Logger().logError(self.__errorClass, self.__error)
            if not lg: print("Error has not been logged")
            del lg
            return False

        return True

    def __isVWindowValid(self, vwindow):
        if type(vwindow) is not int:
            self.__error = '[AP#C3]WINDOW_TYPE_ERROR'
            lg = logger_class.Logger().logError(self.__errorClass, self.__error)
            if not lg: print("Error has not been logged")
            del lg
            return False
        if vwindow > 10:
            self.__error = '[AP#3]WINDOW_VALUE_ERROR'
            lg = logger_class.Logger().logError(self.__errorClass, self.__error)
            if not lg: print("Error has not been logged")
            del lg
            return False

        return True

    def isApplicationValid(self, name, path, vwindow):
        if self.__isNameValid(name) and self.__isPathValid(path) and self.__isVWindowValid(vwindow):
            return True
        else:
            return False

    def __createApplicationDictionary(self, name, path, vwindow):
        self.applicationDictionary = {
            "name": name,
            "path": path,
            "vwindow": vwindow
        }


# app = Application()
# app.createApplication('name', 'path', 3)
# print(app.applicationDictionary)
# del app
