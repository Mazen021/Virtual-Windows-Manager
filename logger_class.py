# app_error
# profile_error

# noinspection SpellCheckingInspection
class Logger:

    __errorClasses = ['app_error', 'profile_error', 'app_error']
    __separator = '_____________________________________\n'

    def logError(self, errorClass, error):
        if type(errorClass) is not str or type(error) is not str:
            print("[LG#C1] ERROR DATA TYPE INVALID")
            return False
        if errorClass not in self.__errorClasses:
            print("[LG#C2] ERROR CLASS NOT RECOGNIZED")
            return False

        if errorClass == self.__errorClasses[0]: return self.__logAppError(error)
        if errorClass == self.__errorClasses[1]: return self.__logProfileError(error)

    def __logAppError(self, appError):
        try:
            appErrorsFile = open('errors/apperrors.txt', 'a')
            appErrorsFile.write(self.__separator + appError + '\n')
            appErrorsFile.close()
            return True
        except:
            # app logging error
            self.__logLoggingError('app_errors', appError)
            print("[LG#2] APP ERROR LOGGING ISSUES")
            return False

    def __logProfileError(self, profileError):
        try:
            profileErrorsFile = open('errors/profileerrors.txt', 'a')
            profileErrorsFile.write(self.__separator + profileError + '\n')
            profileErrorsFile.close()
            return True
        except:
            # profile logging error
            self.__logLoggingError('profile_erros', profileError)
            print("[LG#3] PROFILE ERROR LOGGING ISSUES")
            return False

    def __logLoggingError(self, errorClass, error):
        try:
            loggingErrorsFile = open('errors/loggingerrors.txt', 'a')
            loggingErrorsFile.write(self.__separator + f'Unable to log error [{error}] related to [{errorClass}]')
            loggingErrorsFile.close()
        except:
            print("[LG#C3] CRUCIAL LOGGING ERROR UNABLE TO LOG LOGGING ERROR TERMINATE APPLICATION NOW")


# lg = Logger().logError('profile_error', 'error example')
# print(lg)
#del lg
